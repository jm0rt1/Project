
from __future__ import annotations
from pathlib import Path
from typing import Union
from src.strategy_system.stocks.stock.components.StockComponent import StockComponent


from dataclasses import dataclass
from src.strategy_system.stocks.stock.components.StockComponent import StockComponent


@dataclass
class CashflowReport:
    fiscal_date_ending: str
    reported_currency: str
    operating_cashflow: float
    payments_for_operating_activities: float
    proceeds_from_operating_activities: float
    change_in_operating_liabilities: float
    change_in_operating_assets: float
    depreciation_depletion_and_amortization: float
    capital_expenditures: float
    change_in_receivables: float
    change_in_inventory: float
    profit_loss: float
    cash_flow_from_investment: float
    cash_flow_from_financing: float
    proceeds_from_repayments_of_short_term_debt: float
    payments_for_repurchase_of_common_stock: float
    payments_for_repurchase_of_equity: float
    payments_for_repurchase_of_preferred_stock: float
    dividend_payout: float
    dividend_payout_common_stock: float
    dividend_payout_preferred_stock: float
    proceeds_from_issuance_of_common_stock: float
    proceeds_from_issuance_of_long_term_debt_and_capital_securities_net: float
    proceeds_from_issuance_of_preferred_stock: float
    proceeds_from_repurchase_of_equity: float
    proceeds_from_sale_of_treasury_stock: float
    change_in_cash_and_cash_equivalents: float
    change_in_exchange_rate: float
    net_income: float

    @classmethod
    def from_dict(cls, data: dict[str, str]):
        try:
            proceeds_from_operating_activities = float(data.get(
                "proceedsFromOperatingActivities", ""))
        except ValueError as _:
            proceeds_from_operating_activities = 0
        try:
            proceeds_from_repayments_of_short_term_debt = float(data.get(
                "proceedsFromRepaymentsOfShortTermDebt", ""))
        except ValueError as _:
            proceeds_from_repayments_of_short_term_debt = 0
        try:
            payments_for_repurchase_of_preferred_stock = float(data.get(
                "paymentsForRepurchaseOfPreferredStock", ""))
        except ValueError as _:
            payments_for_repurchase_of_preferred_stock = 0
        try:
            dividend_payout_preferred_stock = float(data.get(
                "dividendPayoutPreferredStock", ""))
        except ValueError as _:
            dividend_payout_preferred_stock = 0

        try:
            proceeds_from_issuance_of_common_stock = float(data.get(
                "proceedsFromIssuanceOfCommonStock", ""))
        except ValueError as _:
            proceeds_from_issuance_of_common_stock = 0

        try:
            proceeds_from_issuance_of_preferred_stock = float(data.get(
                "proceedsFromIssuanceOfPreferredStock", ""))
        except ValueError as _:
            proceeds_from_issuance_of_preferred_stock = 0

        try:
            proceeds_from_sale_of_treasury_stock = float(data.get(
                "proceedsFromSaleOfTreasuryStock", ""))
        except ValueError as _:
            proceeds_from_sale_of_treasury_stock = 0

        try:
            change_in_exchange_rate = float(
                data.get("changeInExchangeRate", ""))
        except ValueError as _:
            change_in_exchange_rate = 0
        try:
            payments_for_operating_activities = float(data.get(
                "paymentsForOperatingActivities", ""))
        except ValueError as _:
            payments_for_operating_activities = 0
        try:
            proceeds_from_issuance_of_long_term_debt_and_capital_securities_net = float(data.get(
                "proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet", ""))
        except ValueError as _:
            proceeds_from_issuance_of_long_term_debt_and_capital_securities_net = 0

        return cls(
            fiscal_date_ending=data.get("fiscalDateEnding", ""),
            reported_currency=data.get("reportedCurrency", ""),
            operating_cashflow=float(data.get("operatingCashflow", "")),
            payments_for_operating_activities=payments_for_operating_activities,
            proceeds_from_operating_activities=proceeds_from_operating_activities,
            change_in_operating_liabilities=float(data.get(
                "changeInOperatingLiabilities", "")),
            change_in_operating_assets=float(
                data.get("changeInOperatingAssets", "")),
            depreciation_depletion_and_amortization=float(data.get(
                "depreciationDepletionAndAmortization", "")),
            capital_expenditures=float(data.get("capitalExpenditures", "")),
            change_in_receivables=float(data.get("changeInReceivables", "")),
            change_in_inventory=float(data.get("changeInInventory", "")),
            profit_loss=float(data.get("profitLoss", "")),
            cash_flow_from_investment=float(
                data.get("cashflowFromInvestment", "")),
            cash_flow_from_financing=float(
                data.get("cashflowFromFinancing", "")),
            proceeds_from_repayments_of_short_term_debt=proceeds_from_repayments_of_short_term_debt,
            payments_for_repurchase_of_common_stock=float(data.get(
                "paymentsForRepurchaseOfCommonStock", "")),
            payments_for_repurchase_of_equity=float(data.get(
                "paymentsForRepurchaseOfEquity", "")),
            payments_for_repurchase_of_preferred_stock=payments_for_repurchase_of_preferred_stock,
            dividend_payout=float(data.get("dividendPayout", "")),
            dividend_payout_common_stock=float(data.get(
                "dividendPayoutCommonStock", "")),
            dividend_payout_preferred_stock=dividend_payout_preferred_stock,
            proceeds_from_issuance_of_common_stock=proceeds_from_issuance_of_common_stock,
            proceeds_from_issuance_of_long_term_debt_and_capital_securities_net=proceeds_from_issuance_of_long_term_debt_and_capital_securities_net,
            proceeds_from_issuance_of_preferred_stock=proceeds_from_issuance_of_preferred_stock,
            proceeds_from_repurchase_of_equity=float(data.get(
                "proceedsFromRepurchaseOfEquity", "")),
            proceeds_from_sale_of_treasury_stock=proceeds_from_sale_of_treasury_stock,
            change_in_cash_and_cash_equivalents=float(data.get(
                "changeInCashAndCashEquivalents", "")),
            change_in_exchange_rate=change_in_exchange_rate,
            net_income=float(data.get("netIncome", "")),
        )


@dataclass
class CashFlow(StockComponent):
    symbol: str
    annual_reports: list[CashflowReport]
    quarterly_reports: list[CashflowReport]

    @ classmethod
    def from_dict(cls, data: dict[str, Union[str, list[dict[str, str]]]]) -> CashFlow:
        annual_reports: list[CashflowReport] = []
        quarterly_reports: list[CashflowReport] = []

        raw_annual_reports: list[dict[str, str]
                                 ] = data.get("annualReports", [])  # type:ignore

        raw_qtrly_reports: list[dict[str, str]
                                ] = data.get("quarterlyReports", [])  # type:ignore

        if type(raw_annual_reports) is str:
            raise TypeError("Annual reports should not be a string")
        if type(raw_qtrly_reports) is str:
            raise TypeError("Quarterly reports should not be a string")

        for report in raw_annual_reports:
            annual_reports.append(CashflowReport.from_dict(report))
        for report in raw_qtrly_reports:
            quarterly_reports.append(CashflowReport.from_dict(report))

        symbol = data.get("symbol", "")
        if type(symbol) is not str:
            raise TypeError("symbol needs to be a string")
        return cls(
            symbol=symbol,
            annual_reports=annual_reports,
            quarterly_reports=quarterly_reports
        )

    @classmethod
    def from_json_file(cls, path: Path):
        return cls.from_dict(cls.load_json_dict(path))
