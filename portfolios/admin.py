from django.contrib import admin
from django.contrib.admin import RelatedFieldListFilter
from . import models
from admin_auto_filters.filters import AutocompleteFilter
from django.contrib.admin.views.main import ChangeList
from django.db.models import Count, Sum


class PortfolioAdmin(admin.ModelAdmin):
    list_display =('name', 'owner')
    list_editable = ['owner']
    
class BrokerAdmin(admin.ModelAdmin):
    list_display =('name', 'slug' )
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['slug']

class AssetFilter(AutocompleteFilter):
    title = 'Asset' # display title
    field_name = 'asset' # name of the foreign key field

class PortfolioAssetSum(ChangeList):
    def get_results(self, *args, **kwargs):
        super(PortfolioAssetSum, self).get_results(*args, **kwargs)
        q = self.result_list.aggregate(portfolio_asset_sum=Sum('total_today_brl'))
        self.portfolio_asset_sum = round(q['portfolio_asset_sum'], 2)

class PortfolioAssetAdmin(admin.ModelAdmin):
    list_display =('asset', 'shares_amount', 'share_average_price_brl','total_cost_brl', 'total_today_brl', 'profit', 'category' )
    list_editable = ['shares_amount', 'share_average_price_brl']
    # list_filter =(('asset__category', RelatedFieldListFilter),)
    list_filter = [AssetFilter, ('asset__category', RelatedFieldListFilter),]

    def get_changelist(self, request):
        return PortfolioAssetSum

class BrokerAssetAdmin(admin.ModelAdmin):
    list_display =('ticker', 'broker', 'shares_amount', 'share_average_price_brl','total_cost_brl', 'total_today_brl' )
    list_editable = ['shares_amount', 'broker', 'share_average_price_brl']
    list_filter =(('portfolio_asset__asset__category', RelatedFieldListFilter), ('broker', RelatedFieldListFilter),)

class TransactionAdmin(admin.ModelAdmin):
    list_display =('date','portfolio','asset','shares_amount', 'share_cost_brl','total_cost_brl', 'order', 'portfolio_avarage_price' )
    list_editable =                  ['shares_amount', 'share_cost_brl', 'order']
    list_filter =(('portfolio_asset__asset__category', RelatedFieldListFilter),)

class PortfolioTokenAdmin(admin.ModelAdmin):
    list_display =('date','portfolio', 'total_today_brl', 'order_value', 'tokens_amount', 'token_price', 'profit_percentage', 'historical_percentage')
    list_filter =(('portfolio', RelatedFieldListFilter),)

    def profit_percentage(self, obj):
        # Return the profit as percentage string
        return str(format(float(obj.profit * 100), '.2f') + ' %')

    def historical_percentage(self, obj):
        # Return the profit as percentage string
        return str(format(float(obj.historical_profit * 100), '.2f') + ' %')

admin.site.register(models.Portfolio, PortfolioAdmin)
admin.site.register(models.Broker, BrokerAdmin)
admin.site.register(models.PortfolioAsset, PortfolioAssetAdmin)
admin.site.register(models.BrokerAsset, BrokerAssetAdmin)
admin.site.register(models.Transaction,TransactionAdmin)
admin.site.register(models.PortfolioToken,PortfolioTokenAdmin)
