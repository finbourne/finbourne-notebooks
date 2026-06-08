# Import modules
import os
import finbourne.sdk.services.lusid as lu
import finbourne.sdk.services.lusid.models as lm
import pandas as pd
from finbourne.sdk.extensions import SyncApiClientFactory, RefreshingToken

# Set the secrets path
secrets_path = os.getenv("FBN_SECRETS_PATH")
if secrets_path is None:
    secrets_path = os.path.join(os.path.dirname(os.getcwd()), "secrets.json")

# Authenticate our user and create our API client
api_factory = SyncApiClientFactory(
    access_token=RefreshingToken(), secrets_path=secrets_path, app_name="LusidJupyterNotebook"
)

aggregation_api = api_factory.build(lu.AggregationApi)
quotes_api = api_factory.build(lu.QuotesApi)
instruments_api = api_factory.build(lu.InstrumentsApi)


def figi_to_lusid(figi):

    instrument = instruments_api.get_instrument(
        identifier_type="Figi", identifier=figi
    )

    return instrument.lusid_instrument_id


def load_eod_prices(scope):

    quotes = [
        ("2018-05-20T23:00:00Z", "BBG000BVPXP1", 106.02),
        ("2018-05-20T23:00:00Z", "BBG000B9XVV8", 131.33),
        ("2018-05-20T23:00:00Z", "BBG000C16621", 112.34),
        ("2018-05-20T23:00:00Z", "BBG000BVL406", 23.44),
        ("2018-05-20T23:00:00Z", "BBG000BTGM43", 53.45),
        ("2018-05-20T23:00:00Z", "BBG00KXXK940", 38.44),
        ("2018-05-20T23:00:00Z", "BBG00JGMWFQ5", 103.44),
        ("2018-05-20T23:00:00Z", "BBG00HPSG933", 44.66),
    ]

    # Create quotes request

    for quote in quotes:

        effective_date = quote[0]
        figi = quote[1]
        price = quote[2]

        luid = figi_to_lusid(figi)

        instrument_quotes = {
            "quotes_1": lm.UpsertQuoteRequest(
                quote_id=lm.QuoteId(
                    quote_series_id=lm.QuoteSeriesId(
                        provider="Lusid",
                        instrument_id=luid,
                        instrument_id_type="LusidInstrumentId",
                        quote_type="Price",
                        field="mid",
                    ),
                    effective_at=effective_date,
                ),
                metric_value=lm.MetricValue(value=price, unit="USD"),
            )
        }

        response = quotes_api.upsert_quotes(scope=scope, request_body=instrument_quotes)


def load_corporate_action_split_price(figi, new_price, effective_date, scope):

        luid = figi_to_lusid(figi)

        instrument_quotes = {
            "quotes_1": lm.UpsertQuoteRequest(
                quote_id=lm.QuoteId(
                    quote_series_id=lm.QuoteSeriesId(
                        provider="Lusid",
                        instrument_id=luid,
                        instrument_id_type="LusidInstrumentId",
                        quote_type="Price",
                        field="mid",
                    ),
                    effective_at=effective_date,
                ),
                metric_value=lm.MetricValue(value=new_price, unit="USD"),
            )
        }

        response = quotes_api.upsert_quotes(scope=scope, request_body=instrument_quotes)


def run_portfolio_valuation(portfolio_code, effective_date, scope):

    val_request = lm.ValuationRequest(
        recipe_id=lm.ResourceId(scope=scope, code="default"),
        metrics=[
            lm.AggregateSpec(key="Instrument/default/Name", op="Value"),
            lm.AggregateSpec(key="Valuation/PvInReportCcy", op="Proportion"),
            lm.AggregateSpec(key="Quotes/Price", op="Value"),
            lm.AggregateSpec(key="Valuation/PvInReportCcy", op="Sum"),
            lm.AggregateSpec(key="Holding/default/Units", op="Sum"),
        ],
        group_by=["Instrument/default/Name"],
        # choose the valuation date for the request - set using effectiveAt
        valuation_schedule=lm.ValuationSchedule(effective_at=effective_date),
        portfolio_entity_ids=[
            lm.PortfolioEntityId(
                scope=scope,
                code=portfolio_code,
                portfolio_entity_type="SinglePortfolio",
            )
        ],
    )

    aggregation = aggregation_api.get_valuation(valuation_request=val_request)

    df = pd.DataFrame(aggregation.data)

    return df
