from open_rarity.resolver.rarity_providers.rarity_sniffer import RaritySnifferResolver


class TestRaritySnifferResolver:
    BORED_APE_COLLECTION_ADDRESS = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"

    def test_get_all_ranks(self):
        token_id_to_ranks = RaritySnifferResolver.get_all_ranks(
            contract_address=self.BORED_APE_COLLECTION_ADDRESS
        )
        assert len(token_id_to_ranks) == 10_000

    def test_get_all_ranks_no_contract(self):
        token_id_to_ranks = RaritySnifferResolver.get_all_ranks(
            contract_address="0x123"
        )
        assert len(token_id_to_ranks) == 0
