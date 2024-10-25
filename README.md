# LUSID Jupyter notebooks

This repository contains Jupyter notebooks that show how to use [LUSID](https://www.finbourne.com/lusid-technology). The examples in this repository are in Python. but the underlying LUSID functionality can be implemented using any language that has a HTTP client library. The notebooks are divided into two categories:

* `features` - Notebooks showing specific LUSID features. These notebooks are short and specific.
* `use-cases` - Notebooks showing sample business implementations or use-cases. These notebooks will combine various LUSID features to solve a business use-case. The `use-case` notebooks are generally longer than the `features` ones.

## analytics/FX
| filename | title | description | features |
| --- | --- | --- | --- |
| [fx-forward-pricing-models.ipynb](<analytics/FX/fx-forward-pricing-models.ipynb>) | FX Forward Pricing Models |  | FX Forwards, Pricing Models, Valuation |
| [fx-inference-triangulation.ipynb](<analytics/FX/fx-inference-triangulation.ipynb>) | FX Inference Triangulation |  | FX, FX inference, Foreign Exchange, Triangulation |


## features/entitlements
| filename | title | description | features |
| --- | --- | --- | --- |
| [Access Metadata entitlements.ipynb](<features/entitlements/Access Metadata entitlements.ipynb>) | Portfolio look-through in LUSID | Demonstrates the use of policies to grant access to portfolios based on their Access Metadata (AMD) in LUSID. | access metadata, amd, entitlements |
| [Portfolio Entitlements.ipynb](<features/entitlements/Portfolio Entitlements.ipynb>) | Portfolio Entitlements | Demonstrates how to create policies/access control to various date items. | entitlements |
| [Property value entitlements.ipynb](<features/entitlements/Property value entitlements.ipynb>) | Portfolio look-through in LUSID | Demonstrates the use of policies to grant access to property values in LUSID. | entitlements, property values, transactions |
| [Restrict Transactions between two effective dates.ipynb](<features/entitlements/Restrict Transactions between two effective dates.ipynb>) | Create Policy to Restrict Portfolio Updates in a Period | This notebook shows how to create a policy to restrict portfolio updates inbetween 2 effective dates by denying any write/delete activity to all portfolios in a given scope. | policies, portfolios |

## engineering-best-practises
| filename | title | description | features |
| --- | --- | --- | --- |
| [Example Data Load.ipynb](<engineering-best-practises/Example Data Load.ipynb>) | Example Data Load | Loads some example data into LUSID | cutlabels, portfolio groups, quotes, transactions, valuation |

## examples/features/core-lusid
| filename | title | description | features |
| --- | --- | --- | --- |
| [Bi-temporal example.ipynb](<features/bi-temporality/Bi-temporal example.ipynb>) | Bi-temporal Example | Demonstration of how the asAt date can be used to get data from different system dates. | bi-temporality, cocoon - identify_cash_items, holdings, transaction configuration, transactions |
| [Cancelling transactions in LUSID.ipynb](<product/ibor/Cancelling transactions in LUSID.ipynb>) | Cancelling transactions | Demonstration of how to use the CancelTransactions endpoint to cancel transactions in a LUSID portfolio. | cancel transactions, cocoon - seed_data, holdings, transactions |
| [Derived portfolios.ipynb](<product/ibor/Derived portfolios.ipynb>) | Derived portfolios | Shows how to use derived portfolios, a type of portfolio that inherits the contents from a parent portfolio. | derived portfolios, holdings, transactions |
| [Generating an IBOR extract with LUSID's GetHoldings method.ipynb](<product/ibor/Generating an IBOR extract with LUSID's GetHoldings method.ipynb>) | Generating an IBOR extract | Demonstrates how to use the GetHoldings API to generate IBOR extracts. | cocoon - seed_data, holdings |
| [Multi-Value Properties.ipynb](<product/edm/Multi-Value Properties.ipynb>) | Time-variant Properties (e.g. coupon schedule) in LUSID  | Illustrates the use of multi-value properties. | coupon schedules, multi-valued properties, time-variant properties |
| [Output Transactions.ipynb](<product/ibor/Output Transactions.ipynb>) | Output Transactions | This notebook shows how LUSID uses synthetic transactions to fill in the gaps between user-instructed transactions and corporate actions. | adjust holdings, build transactions, corporate actions, instruments, output transactions, portfolios, stock split, sub-holding keys, transactions |
| [Paging and limiting LUSID's API calls.ipynb](<engineering-best-practises/Paging and limiting LUSID's API calls.ipynb>) | Paging and limiting LUSID's API calls | Shows how to slice up large requests to LUSID into smaller requests using the limit and page parameters. | paging |
| [Processing Corporate Actions as native LUSID transitions.ipynb](<product/ibor/Processing Corporate Actions as native LUSID transitions.ipynb>) | Processing Corporate Actions using LUSID transitions | Demonstration of booking corporate actions using LUSID's transitions | cocoon - seed_data, corporate actions, holdings, transaction configuration, transactions |
| [Sub-holding Keys.ipynb](<product/ibor/Sub-holding Keys.ipynb>) | Sub-Holding Keys | Demonstration of how to set up and use sub-holding keys | cocoon - seed_data, holdings, properties, prorated, sub-holding keys |
| [TimeVariant Properties.ipynb](<product/edm/TimeVariant Properties.ipynb>) | Time-variant Properties (e.g. coupon schedule) in LUSID  | Illustrates the use of time-variant properties, a type of property that depend on different effective dates. | coupon schedules, multi-valued properties, time-variant properties |

## product/edm/relations
| filename | title | description | features |
| --- | --- | --- | --- |
| [Relations.ipynb](<product/edm/Relations.ipynb>) | Relations | Demonstrates how to create relationships between different portfolios. | relations |

## features/horizon/data-feeds
| filename | title | description | features |
| --- | --- | --- | --- |
| [Using TraderMade FX spot price data in LUSID.ipynb](<features/horizon/Using TraderMade FX spot price data in LUSID.ipynb>) | Using TraderMade FX spot price data in LUSID | This notebook shows you how to access TraderMade spot FX data in LUSID | quotes |

## modules
| filename | title | description | features |
| --- | --- | --- | --- |
| [Valuation.ipynb](<product/ibor/Valuation.ipynb>) | Valuation | Demonstrates how to value a portfolio using a custom recipe. | valuation |
| [bitemporal-backtrade.ipynb](<features/bi-temporality/bitemporal-backtrade.ipynb>) | Bi-temporal backtrade | Demonstrates how to add a missing trade and then get back transactions using the AsAt date. | bi-temporality |

## use-cases/abor
| filename | title | description | features |
| --- | --- | --- | --- |
| [Create and Setup Chart of Accounts and General Ledger Accounts.ipynb](<product/abor/Create and Setup Chart of Accounts and General Ledger Accounts.ipynb>) | Corporate Actions in LUSID |  | Accounts, Chart of Accounts, Properties |
| [Generate P&L with different accounting methods (FIFO and LIFO).ipynb](<product/abor/Generate P&L with different accounting methods (FIFO and LIFO).ipynb>) | Accounting methods | Generating P&L with different accounting methods (FIFO and LIFO) | accounting methods, cocoon, derived portfolios, transaction configuration |
| [Using Custodian Accounts.ipynb](<product/abor/Using Custodian Accounts.ipynb>) | Custodian Accounts in LUSID |  | custodian accounts, transaction portfolios, transactions |

## audit-trail
| filename | title | description | features |
| --- | --- | --- | --- |
| [Identifying Downstream Consumers affected by Backdated Corrections on a Locked Reporting Window.ipynb](<product/abor/Identifying Downstream Consumers affected by Backdated Corrections on a Locked Reporting Window.ipynb>) | Identifying backdated corrections | Demonstration of how to identify backdated corrections and their impact | build transaction, cocoon - seed_data, insights, portfolio changes |
| [Requesting log details using the Insights API.ipynb](<engineering-best-practises/Requesting log details using the Insights API.ipynb>) | Requesting details of inline valuation operations using the insights API |  | Insights, Request Logs |

## cash-management
| filename | title | description | features |
| --- | --- | --- | --- |
| [Booking subscriptions and redemptions.ipynb](<product/ibor/Booking subscriptions and redemptions.ipynb>) | Booking subscriptions and redemptions | Demonstration of how to model subscriptions and redemptions in LUSID | cocoon - seed_data, holdings, transaction configuration |
| [Manual journal entries to correct cash balances.ipynb](<product/ibor/Manual journal entries to correct cash balances.ipynb>) | Correcting cash balances with manual journal entries | Demonstration of how to model manual journal entries in LUSID | cancel transactions, cocoon, holdings, reconciliations, transaction configuration |

## change-management
| filename | title | description | features |
| --- | --- | --- | --- |
| [Business Agility - migration between investment systems.ipynb](<engineering-best-practises/Business Agility - migration between investment systems.ipynb>) | Business agility | Demonstration of how to migrate your data from one system to another. | holdings, instruments, properties, reconciliations, set holdings, transaction configuration, transactions |
| [Checking a portfolio for transaction updates since an AsAt time.ipynb](<product/ibor/Checking a portfolio for transaction updates since an AsAt time.ipynb>) | Checking a portfolio for transaction updates since an AsAt time |  | AsAt, GetPortfolioChanges API, Transaction Portfolios |
| [Safely and efficiently test changes to your system.ipynb](<engineering-best-practises/Safely and efficiently test changes to your system.ipynb>) | Testing system changes | Demonstration of how to safely test changes to your data in a production environment | derived portfolios, instrument definitions, instruments, set holdings, transactions |
| [Set up a sandbox trading environment.ipynb](<engineering-best-practises/Set up a sandbox trading environment.ipynb>) | Sandbox trading environment | Learn how to setup a virtual trading environment in LUSID. | aggregation, instruments, properties, quotes, reference portfolios, set holdings, transactions |

## product/compliance
| filename | title | description | features |
| --- | --- | --- | --- |
| [Configuring and Running Pre-Trade Compliance.ipynb](<product/compliance/Configuring and Running Pre-Trade Compliance.ipynb>) | Compliance in LUSID |  | Compliance, OMS, Pre/Post trade checks |

## product/ibor
| filename | title | description | features |
| --- | --- | --- | --- |
| [Corporate Actions.ipynb](<product/ibor/Corporate Actions.ipynb>) | Equity - Handling Corporate Actions |  | bonus issue, corporate actions, dividend, equity, merger, recipes, spin-off, split, valuations |
| [Creating Portfolios With Different Tax Lot Management Methods.ipynb](<product/abor/Creating Portfolios With Different Tax Lot Management Methods.ipynb>) | Creating portfolios with different tax lot management methods | This notebook demonstrates how to create transaction portfolios under different tax lot accounting methodologies. | accounting, corporate actions, holdings, taxlots, transactions |
| [Generating Corporate actions natively in LUSID.ipynb](<product/ibor/Generating Corporate actions natively in LUSID.ipynb>) | Corporate Actions in LUSID | Demonstrates how to create and apply a corporate action to a portfolio. | corporate actions, derived portfolios, holdings, transactions |
| [Generating holdings with the movements engine in LUSID.ipynb](<product/ibor/Generating holdings with the movements engine in LUSID.ipynb>) | Generating holdings | Generating holdings with the movements engine | cocoon, instruments, transaction configuration, transactions |
| [Get Holdings and Extract to csv.ipynb](<product/ibor/Get Holdings and Extract to csv.ipynb>) | Get Holdings | Shows how to use the Get Holdings endpoint and extract it to a csv | holdings, transaction portfolios |
| [Get a consolidated view of your data from multiple systems.ipynb](<product/ibor/Get a consolidated view of your data from multiple systems.ipynb>) | Consolidating multiple systems | Demonstration of how to migrate funds from multiple source systems into LUSID | aggregation, holdings, instruments, properties, quotes, reconciliations, transaction configuration |
| [How do I create holdings in LUSID.ipynb](<product/ibor/How do I create holdings in LUSID.ipynb>) | Creating holdings in LUSID | Demonstrates how to load transactions based on custom transaction types and then compute the subsequent holdings. | properties, transaction configuration, transactions |
| [IBOR User Journey.ipynb](<product/ibor/IBOR User Journey.ipynb>) | IBOR User Journey | A day in the life of an IBOR using LUSID | aggregation, aggregation, cocoon, corporate actions, instruments, quotes, results store, sub-holding keys, transaction configuration, valuation reconciliation |
| [Load Transactions from an External System.ipynb](<product/ibor/Load Transactions from an External System.ipynb>) | Loading transactions from an external system | Demonstration of loading a transaction XML file from another "External System" into LUSID. | cocoon, holdings, transactions |
| [Loading data with the Lusid-Python-Tools (LPT) package.ipynb](<engineering-best-practises/Loading data with the Lusid-Python-Tools (LPT) package.ipynb>) | Loading data with LUSID Python Tools | Demonstrates how to load portfolios, instruments, holdings, and transactions. | cocoon, instruments, portfolios, transactions |
| [Maintain a fund in multiple currencies and share classes.ipynb](<product/abor/Maintain a fund in multiple currencies and share classes.ipynb>) | Modelling share classes in LUSID | This notebook shows how to model a fund that operates in different currencies and share classes. | adjust holdings, aggregation, holdings, instrument definitions, quotes, transactions |
| [Maintaining an instrument master in LUSID.ipynb](<product/edm/Maintaining an instrument master in LUSID.ipynb>) | Maintaining an instrument master | Demonstrates how to import, update, retrieve, and delete instruments. | instruments, properties, search |
| [Perform a reconciliation.ipynb](<product/ibor/Perform a reconciliation.ipynb>) | Reconciliations | Demonstration of how to use LUSID to find discrepancies between versions of a portfolio | adjust holdings, instruments, portfolio groups, properties, reconciliations, set holdings, transactions |
| [Portfolio types and portfolio groups in LUSID.ipynb](<product/ibor/Portfolio types and portfolio groups in LUSID.ipynb>) | Portfolios and Portfolio Groups | Demonstrates how to do various operations with portfolios and portfolio groups. | commands, corporate actions, portfolio groups, portfolios, transactions |
| [Running a Global Fund.ipynb](<product/ibor/Running a Global Fund.ipynb>) | Running a global fund | Demonstration of using LUSID to run funds fed from multiple source systems across multiple regions | aggregation, cocoon, cut labels, instruments, quotes, recipes, transaction configuration, transactions |
| [Using cut-labels to manage your business across different time-zones.ipynb](<product/ibor/Using cut-labels to manage your business across different time-zones.ipynb>) | Cut Labels | Demonstrates how to use cut labels to simplify timestamps and streamline usage of LUSID when used across multiple timezones. | cut labels, holdings, instruments, transactions |

## features/instruments
| filename | title | description | features |
| --- | --- | --- | --- |
| [Bond.ipynb](<features/instruments/Bond.ipynb>) | Bonds - Computing P&amp;L and Accrued Interest for Bonds |  | P&amp;L, accrued interest, bond, bonds, recipes, valuations |
| [BondWithAmortisation.ipynb](<features/instruments/BondWithAmortisation.ipynb>) | Bonds - Amortisation |  | P&amp;L, a2b, amortisation, amortization, bond |
| [Contract for Difference.ipynb](<features/instruments/Contract for Difference.ipynb>) | Contract for Difference - Calculating Intraday P&amp;L for CFD's with and without Daily Close outs |  | P&amp;L, cfd, close out, contract for difference, recipes, valuations |
| [Equity Option.ipynb](<features/instruments/Equity Option.ipynb>) | Equity Option - Booking and valuing an Equity Option with physical settlement |  | P&amp;L, equity option, physical settlement, recipes, valuations |
| [Equity Options - Pricing and risk using Black-Scholes.ipynb](<features/instruments/Equity Options - Pricing and risk using Black-Scholes.ipynb>) | Equity Option - Pricing and risk |  | black scholes, equity option, exposure, inline valuations, market value, option delta |
| [FX Forward.ipynb](<features/instruments/FX Forward.ipynb>) | FX Forward - Valuation Workflow |  | FX Forwards, complex market data, recipes, valuations |
| [Funding Leg Swap.ipynb](<features/instruments/Funding Leg Swap.ipynb>) | Variable Funding Leg + Equity or Cash Instrument | Demonstrates creation and pricing of a funding leg with <br>variable notional and constructing a related position in<br>an stock or underlying instrument. This construct can be used<br>to represent the mechanics of a total return or equity swap. | aggregation, funding leg swap, instruments, market data store, quotes, results store |
| [Interest Rate Swap.ipynb](<features/instruments/Interest Rate Swap.ipynb>) | Interest Rate Swap Valuation | Demonstrates pricing of an Interest Rate Swap based on a user defined Instrument. | instruments, lifecycle events, market data store, quotes, results store, valuation |
| [Mortgage Backed Securities.ipynb](<features/instruments/Mortgage Backed Securities.ipynb>) | Mortgage Backed Securities in LUSID |  | complex bond, mbs, mortgage backed securities, pool factor, schedule |
| [Simple Equity.ipynb](<features/instruments/Simple Equity.ipynb>) | Equity - Computing P&amp;L and Handling Dividends for Equities |  | P&amp;L, dividend, equity, recipes, valuations |
| [Term Deposit.ipynb](<features/instruments/Term Deposit.ipynb>) | Term Deposit Valuation | Demonstrates pricing of a Term Deposit Investment. | instruments, lifecycle events, market data store, quotes, results store, valuation |

## models-and-indices
| filename | title | description | features |
| --- | --- | --- | --- |
| [Rebalancing with a model portfolio.ipynb](<product/pms/Rebalancing with a model portfolio.ipynb>) | Rebalancing with a model portfolio  | This notebook shows how you can automatically generate transactions to rebalance a transaction portfolio with a model portfolio | reference portfolios, transactions portfolios |
| [Setting up a blended benchmark with floating weights.ipynb](<product/pms/Setting up a blended benchmark with floating weights.ipynb>) | Setting up a blended benchmark | Demonstration of how to load a blended benchmark. <br>We also show how floating weights with a periodic reset. | Floating weights, Reference portfolios, Securitised portfolios, Weights |

## orders-management
| filename | title | description | features |
| --- | --- | --- | --- |
| [Incorporating live orders into your holdings view.ipynb](<product/oms/Incorporating live orders into your holdings view.ipynb>) | Live Orders with Holdings in LUSID |  | holdings, instruments, orders, portfolio, quotes, recipe |

## portfolio-construction
| filename | title | description | features |
| --- | --- | --- | --- |
| [Call Api On File Upload.ipynb](<features/workflow/Call Api On File Upload.ipynb>) | Call Api on File Upload |  | events, luminesce, notifications, subscriptions |

## post-trade-processing
| filename | title | description | features |
| --- | --- | --- | --- |
| [Managing a transaction lifecycle using LUSID's properties.ipynb](<features/instruments/Managing a transaction lifecycle using LUSID's properties.ipynb>) | Managing the transaction lifecycle on LUSID | Demonstration of how to use properties to manage the transaction lifecycle | cocoon, data types, instruments, properties, transactions |
| [Transactions with Trade To Portfolio Rate.ipynb](<product/ibor/Transactions with Trade To Portfolio Rate.ipynb>) | Trade To Portfolio Rate (TTPR) Demo | This notebook demonstrates how LUSID can resolve the Trade To Portfolio Rate for transactions booked with different trade currencies to the base portfolio currency. | instruments, portfolios, quotes, recipes, trade to portfolio rate, transactions |

## private-assets
| filename | title | description | features |
| --- | --- | --- | --- |
| [Managing cashflows - capital calls and income distributions.ipynb](<product/ibor/Managing cashflows - capital calls and income distributions.ipynb>) | Running a Fund with Investors | Demonstration of how to manage a fund's subscriptions and capital calls with investors in LUSID | holdings, instruments, properties, transaction configuration, transactions |
| [Supporting a multi-asset class book of business.ipynb](<product/ibor/Supporting a multi-asset class book of business.ipynb>) | Bespoke asset classes | Demonstration of how to create your own custom instrument inside LUSID, create a transaction against it and value it. | aggregation, instruments, properties, quotes, transactions |

## private-markets
| filename | title | description | features |
| --- | --- | --- | --- |
| [Private Markets and Real Estate.ipynb](<product/ibor/Private Markets and Real Estate.ipynb>) | Private Markets and Real Estate |  | cash flows, excel, lookthrough, pdf, private markets, quotes, real estate, transactions |

## risk-and-performance
| filename | title | description | features |
| --- | --- | --- | --- |
| [Backtesting with LUSID derived portfolios.ipynb](<product/ibor/Backtesting with LUSID derived portfolios.ipynb>) | Backtesting with derived portfolios | Shows how to use a derived portfolio to test different trading strategies. | aggregation, cocoon, derived portfolios, holdings, instruments, quotes |
| [Calculating P&amp;L on strategy.ipynb](<product/ibor/Calculating P&L on strategy.ipynb>) | Calculating P&amp;L on strategies | Demonstration of how to use sub-holding keys and output transactions to track P&L on different strategies. | cocoon - seed_data, derived portfolios, output transactions, properties, sub-holding keys, transactions |
| [Composite returns adjusted for FX rates.ipynb](<product/ibor/Composite returns adjusted for FX rates.ipynb>) | Loading and caculating returns | Demonstration of how to get aggregate returns adjusted by FX performance | Composite portfolios, FX performance, Returns |
| [Loading and calculating returns.ipynb](<product/ibor/Loading and calculating returns.ipynb>) | Loading and calculating returns | Demonstration of how to load and calculate returns in LUSID. | Returns |
| [Manage your investment strategies.ipynb](<product/ibor/Manage your investment strategies.ipynb>) | Managing investment strategies | Demonstration of how to compare how strategies are performing across all of our client's holdings, rather than just looking at a single portfolio in isolation. | aggregation, data types, instruments, portfolio groups, properties, set holdings, transactions |
| [Returns on composite portfolios.ipynb](<product/ibor/Returns on composite portfolios.ipynb>) | Loading and caculating returns | Demonstration of how to load and calculate returns on composite portfolios in LUSID | Composite portfolios, Returns |
| [Track trading commissions in your portfolio.ipynb](<product/ibor/Track trading commissions in your portfolio.ipynb>) | Track trading costs and commissions in your portfolio | Demonstrates how to track commissions and fees separately from trade costs. | cocoon, instruments, portfolio groups, properties, sub-holding keys, transaction configuration, transactions |

## valuation
| filename | title | description | features |
| --- | --- | --- | --- |
| [Bond Pricing And Accrued Interest Calculation.ipynb](<features/instruments/Bond Pricing And Accrued Interest Calculation.ipynb>) | Bond Pricing And Accrued Interest Calculation | Demonstrates pricing a bond and calculating it's accrued interest based on a user defined Bond Instrument. | aggregation, instruments, market data store, quotes, results store |
| [Configuration Recipe Composability Using Recipe Composer.ipynb](<product/ibor/Configuration Recipe Composability Using Recipe Composer.ipynb>) | Recipe Composer Workflow |  | recipe composers, recipes, valuations |
| [Externally Calculated Metrics.ipynb](<product/ibor/Externally Calculated Metrics.ipynb>) | Save externally calculated metrics and use them within the Valuation Engine | Attributes<br>---------- |  |
| [FundingLeg Valuation with compounding interests.ipynb](<features/instruments/FundingLeg Valuation with compounding interests.ipynb>) | FundingLeg - Valuation with daily resets |  | Compounding, FundingLeg, recipes, valuations |
| [Futures Valuation with Differing Cost Basis Treatments (Synthetic Cash Method).ipynb](<features/instruments/Futures Valuation with Differing Cost Basis Treatments (Synthetic Cash Method).ipynb>) | Futures Valuation Workflow |  | futures, recipes, transaction types, valuations |
| [Futures Valuation with Differing Cost Basis Treatments.ipynb](<features/instruments/Futures Valuation with Differing Cost Basis Treatments.ipynb>) | Futures Valuation Workflow |  | futures, recipes, transaction types, valuations |
| [Futures Valuation with notional cost and variation margin.ipynb](<features/instruments/Futures Valuation with notional cost and variation margin.ipynb>) | Futures Valuation Workflow |  | futures, recipes, transaction types, valuations |
| [Look-through valuation.ipynb](<product/ibor/Look-through valuation.ipynb>) | Portfolio look-through in LUSID | Shows how to compute the value of a child portfolio's holding as though they were directly held by the parent portfolio. | holdings, look through, portfolios, securitised portfolios, valuations |
| [Model selection using instrument features and properties.ipynb](<product/ibor/Model selection using instrument features and properties.ipynb>) | Model selection using instrument features and properties | Demonstration of how to configure model selectio for valuation based on instrument features as well as instrument properties. | Derived instrument properties, Instrument features, Instruments, Model selection |
| [Real-time Valuation.ipynb](<product/ibor/Real-time Valuation.ipynb>) | Real-time valuation using streamed market data | This notebook shows how to value a portfolio using real-time streamed market data | recipes, valuation |
| [SRS csv Example.ipynb](<product/ibor/SRS csv Example.ipynb>) | Structured Results Store for storage of Portfolio data |  | luminesce, structured_results_store, virtual_document |
| [Simple Valuation.ipynb](<product/ibor/Simple Valuation.ipynb>) | Simple valuation with default recipes | This notebook shows how to value a portfolio using recipes, for an out of the box look at positions and valuations | manifests, recipes, transactions, valuation |
| [Total Return Swap Pricing With Reference Instrument.ipynb](<features/instruments/Total Return Swap Pricing With Reference Instrument.ipynb>) | Total Return Swap Pricing With Reference Instrument | Demonstrates pricing of an Total Return Swap with AssetLeg having the ReferenceInstrument as underlying. | instruments, reference-instrument, valuation |
| [Valuation Analysis.ipynb](<product/pms/Valuation Analysis.ipynb>) | Valuation Debugging |  | instruments, recipes, transactions, valuation, valuation manifest |
| [Valuations with recipes.ipynb](<product/ibor/Valuations with recipes.ipynb>) | Valuation with recipes | This notebook shows how to value a portfolio using recipes with different pricing sources | manifests, recipes, transactions, valuation |

## wealth-management
| filename | title | description | features |
| --- | --- | --- | --- |
| [Households.ipynb](<product/pms/Households.ipynb>) | Households | Demonstration of how to manage the holdings for an investor based on each Mandate & Household they are associated with. | aggregation, instruments, portfolio groups, portfolios, properties, quotes, set holdings |

## university/T02002-Luminesce-syntax
| filename | title | description | features |
| --- | --- | --- | --- |
| [Luminesce Syntax.ipynb](<university/T02002-Luminesce-syntax/Luminesce Syntax.ipynb>) | Luminesce Syntax | Attributes<br>---------- |  |

## university/T02003-Luminesce-Providers-and-Views
| filename | title | description | features |
| --- | --- | --- | --- |
| [Providers and Views.ipynb](<university/T02003-Luminesce-Providers-and-Views/Providers and Views.ipynb>) | Luminesce Providers and Views | Attributes<br>---------- |  |


| :warning: This file is generated, any direct edits will be lost. For instructions on how to generate the file, see [docgen/README](../docgen/). |
| --- |

