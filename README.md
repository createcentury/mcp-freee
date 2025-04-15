# mcp-freee

freee API用のModel Context Protocol (MCP) サーバー実装です。AIアシスタントがfreeeの会計データにアクセスできるようにするためのブリッジとして機能します。

## 概要

このプロジェクトは、[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) を使用して、freee APIへのアクセスを提供します。MCPは、AIアシスタントが外部システムやAPIと安全に通信するための標準プロトコルです。

## 機能

このMCPサーバーは以下のfreee APIエンドポイントにアクセスできます：

- 事業所情報の取得
- 取引先一覧の取得
- 特定の取引先に関連する取引の取得
- 請求書一覧の取得
- 口座明細（支払履歴）の取得
- 損益計算書の取得
- 仕訳帳PDFの出力リクエストと取得

## セットアップ方法

### 前提条件

- Python 3.8以上
- freee APIアクセストークン
- freee事業所ID

### インストール

1. リポジトリをクローンします：

```bash
git clone https://github.com/createcentury/mcp-freee.git
cd mcp-freee
```

2. 依存パッケージをインストールします：

```bash
pip install mcp-python httpx
```

### Claude Desktopでの設定

Claude Desktopアプリで使用するには、以下の設定を行います：

1. Claude Desktopの設定ファイルを開きます：
   `/Users/[ユーザー名]/Library/Application Support/Claude/claude_desktop_config.json`

2. 以下の設定を追加します：
   アクセストークンと事業者IDは公式サイトから取得して下さい。
   https://accounts.secure.freee.co.jp/login/app_store/developers

```json
{
  "mcp_servers": {
    "freee-mcp": {
      "command": "/Users/[ユーザー名]/miniconda3/bin/python",
      "args": [
        "/Users/[ユーザー名]/Downloads/freee_mcp/freee_mcp.py"
      ],
      "env": {
        "FREEE_ACCESS_TOKEN": "あなたのアクセストークン",
        "FREEE_COMPANY_ID": "あなたの事業所ID"
      }
    }
  }
}
```

## セキュリティに関する免責事項

**重要**: このツールは、freee APIへのアクセスを提供するため、財務データや事業情報などの機密情報を扱います。以下の点に注意してください：

- このツールは「現状のまま」提供され、いかなる保証もありません
- アクセストークンや事業所IDなどの認証情報は適切に保護してください
- 本番環境での使用は自己責任で行ってください
- 情報セキュリティ、データプライバシー、およびコンプライアンスに関する責任は利用者にあります
- freee APIの利用規約に従って使用してください

## ライセンス

MIT

## 貢献

プルリクエストや問題報告は歓迎します。大きな変更を加える前に、まずissueを開いて議論することをお勧めします。
