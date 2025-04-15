from mcp.server.fastmcp import FastMCP, Context
import httpx
from typing import Dict, Any

# MCPサーバーの初期化
mcp = FastMCP("freee")

BASE_URL = "https://api.freee.co.jp"

import os

ACCESS_TOKEN = os.environ["FREEE_ACCESS_TOKEN"]
COMPANY_ID = os.environ["FREEE_COMPANY_ID"]


headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

@mcp.tool()
async def get_company_info(ctx: Context = None) -> Dict[str, Any]:
    """Freeeの事業所情報を取得する"""
    url = f"{BASE_URL}/api/1/companies/{COMPANY_ID}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def list_partners(limit: int = 10, ctx: Context = None) -> Dict[str, Any]:
    """Freeeの取引先を一覧取得する"""
    url = f"{BASE_URL}/api/1/partners?company_id={COMPANY_ID}&limit={limit}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    
@mcp.tool()
async def get_deals_by_partner(partner_id: int, ctx: Context = None) -> Dict[str, Any]:
    """
    指定したpartner_idに紐づく取引を取得します。
    """
    url = f"{BASE_URL}/api/1/deals"
    params = {
        "company_id": COMPANY_ID,
        "partner_id": partner_id,
        "limit": 20
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def list_invoices(ctx: Context = None) -> Dict[str, Any]:
    """請求書一覧を取得します。"""
    url = f"{BASE_URL}/api/1/invoices"
    params = {"company_id": COMPANY_ID}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def list_wallet_txns(ctx: Context = None) -> Dict[str, Any]:
    """口座明細（支払履歴）を取得します。"""
    url = f"{BASE_URL}/api/1/wallet_txns"
    params = {"company_id": COMPANY_ID}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def get_trial_pl(ctx: Context = None) -> Dict[str, Any]:
    """損益計算書を取得します（当期分）。"""
    url = f"{BASE_URL}/api/1/reports/trial_pl"
    params = {"company_id": COMPANY_ID}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

@mcp.tool()
async def request_journal_pdf(ctx: Context = None) -> Dict[str, Any]:
    """仕訳帳PDF出力をリクエストします。"""
    url = f"{BASE_URL}/api/1/journals"
    params = {"company_id": COMPANY_ID}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()  # この中の reports[0]["id"] を次で使う

@mcp.tool()
async def download_journal_pdf(report_id: str, ctx: Context = None) -> bytes:
    """指定されたレポートIDから仕訳帳PDFをダウンロードします。"""
    url = f"{BASE_URL}/api/1/journals/reports/{report_id}/download"
    headers_pdf = headers.copy()
    headers_pdf["Accept"] = "application/pdf"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers_pdf)
        response.raise_for_status()
        return response.content  # Claudeにはバイナリ送信不可なので変換が必要


if __name__ == "__main__":
    mcp.run()
