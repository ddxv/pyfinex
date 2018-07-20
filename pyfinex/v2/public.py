# REST PUBLIC ENDPOINTS ###################################################
    def platform_status(self, **params):
        """ Get the current status of the platform. Maintenance periods last for just few minutes and might be necessary 
        from time to time during upgrades of core components of our infrastructure.
        Docs: https://bitfinex.readme.io/v2/reference#rest-public-platform-status
        """
        endpoint = 'platform/status'
        return self.request(endpoint, method='GET', auth=False, params=params)
    
    def tickers(self, **params):
        """ The ticker is a high level overview of the state of the market. It shows you the current best bid and ask, as well as the last trade price. It also includes information such as daily volume and how much the price has moved over the last day.
        Docs: https://bitfinex.readme.io/v2/reference#rest-public-tickers
        """
        endpoint = 'tickers'
        return self.request(endpoint, method='GET', auth=False, params=params)

    def ticker(self, **params):
        """ The ticker is a high level overview of the state of the market. It shows you the current best bid and ask, as well as the last trade price. It also includes information such as daily volume and how much the price has moved over the last day.
        Docs: https://bitfinex.readme.io/v2/reference#rest-public-ticker
        """
        endpoint = 'ticker/' + params.pop('Symbol')
        return self.request(endpoint, method='GET', auth=False, params=params)

    def trades(self, **params):
        """ Trades endpoint includes all the pertinent details of the trade, such as price, size and time.
        Docs: https://bitfinex.readme.io/v2/reference#rest-public-trades
        """
        endpoint = 'trades/' + params.pop('Symbol') + '/hist'
        return self.request(endpoint, method='GET', auth=False, params=params)

    def books(self, **params):
        """ The Order Books channel allow you to keep track of the state of the Bitfinex order book. It is provided on a price aggregated basis, with customizable precision.
        Docs: https://bitfinex.readme.io/v2/reference#rest-public-books
        """
        endpoint = 'book/' + params.pop('Symbol') + '/' + params.pop('Precision')
        return self.request(endpoint, method='GET', auth=False, params=params)

    def stats(self, **params):
        """ Various statistics about the requested pair.
        Docs: https://bitfinex.readme.io/v2/reference#rest-public-stats
        """
        endpoint = 'stats1/' + params.pop('Key') + ':' + params.pop('Size') + ':' + params.pop('Symbol') + '/' + params.pop('Section')
        return self.request(endpoint, method='GET', auth=False, params=params)

    def candles(self, **params):
        """ Various statistics about the requested pair.
        Docs: https://bitfinex.readme.io/v2/reference#rest-public-candles
        """
        endpoint = 'candles/trade:' + params.pop('TimeFrame') + ':' + params.pop('Symbol') + '/' + params.pop('Section')
        return self.request(endpoint, method='GET', auth=False, params=params)