class AssetSelector:
    def __init__(self, client):
        self.client = client

    def get_open_assets(self):
        data = self.client.api.get_all_open_time()
        digital_assets = data.get("digital", {})

        open_assets = []
        for asset, info in digital_assets.items():
            if info.get("open"):
                open_assets.append(asset)

        return open_assets

    def get_payout(self, asset):
        try:
            payout = self.client.api.get_digital_payout(asset)
            return payout if payout else 0
        except Exception:
            return 0

    def get_best_asset(self):
        assets = self.get_open_assets()

        best_asset = None
        best_payout = 0

        for asset in assets:
            payout = self.get_payout(asset)
            print(f"Asset: {asset} | Payout: {payout}")

            if payout > best_payout:
                best_payout = payout
                best_asset = asset

        print(f"🔥 Best Asset: {best_asset} | Payout: {best_payout}")

        return best_asset, best_payout
