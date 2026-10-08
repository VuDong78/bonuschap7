def calculate_flower_price(da_lat_qty, sapa_qty):
    BASE_PRICE = 100000 
    da_lat_price = BASE_PRICE * (1 - 0.15) 
    da_lat_revenue = da_lat_qty * da_lat_price
    
    sapa_price = BASE_PRICE 
    sapa_revenue = sapa_qty * sapa_price
    
    total_revenue = da_lat_revenue + sapa_revenue
    
    return da_lat_revenue, sapa_revenue
def get_cumulative_statistics(da_lat_stat_qty=0, sapa_stat_qty=0, da_lat_stat_value=0.0,sapa_stat_value=0.0, previous_stats=None):
    if previous_stats is None:
        previous_stats = {
            'da_lat_stat_qty': 0,
            'da_lat_stat_value': 0.0,
            'sapa_stat_qty': 0,
            'sapa_stat_value': 0.0,
            'total_revenue': 0.0
        }
    total_da_lat_qty = previous_stats['da_lat_stat_qty'] + da_lat_stat_qty
    total_sapa_qty = previous_stats['sapa_stat_qty'] + sapa_stat_qty
    total_da_lat_value = previous_stats['da_lat_stat_value'] + da_lat_stat_value
    total_sapa_value = previous_stats['sapa_stat_value'] + sapa_stat_value
    total_revenue = total_da_lat_value + total_sapa_value
    
    return {
        'da_lat_stat_qty': total_da_lat_qty,
        'da_lat_stat_value': total_da_lat_value,
        'sapa_stat_qty': total_sapa_qty,
        'sapa_stat_value': total_sapa_value,
        'total_revenue': total_revenue
    }