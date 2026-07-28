"""
Module-specific configurations for SalesAI.
Each key is a module name. The 'analyses' list defines available drill-down views.
No calculation_steps are used — data is fetched directly from the data layer.
"""

MODULES_DATA = {
    "sales": {
        "icon": "📊",
        "color": "#1565C0",
        "gradient": "linear-gradient(135deg, #1565C0 0%, #42A5F5 100%)",
        "description": "Track invoices, orders, and sales performance",
        "analyses": [
            {
                "name": "Invoice",
                "type": "sales_invoice",
                "description": "Invoice tracking and analysis",
            },
            {
                "name": "Orders",
                "type": "sales_orders",
                "description": "Order volume and trends",
            },
            {
                "name": "Net Sales & Gross Sales",
                "type": "sales_net_gross",
                "description": "Net and gross sales performance",
            },
        ],
    },
    "salesforce": {
        "icon": "👤",
        "color": "#6A1B9A",
        "gradient": "linear-gradient(135deg, #6A1B9A 0%, #AB47BC 100%)",
        "description": "Monitor field force visits, trainings, and tour plans",
        "analyses": [
            {
                "name": "Visits",
                "type": "salesforce_visits",
                "description": "Field force visit metrics",
            },
            {
                "name": "Trainings",
                "type": "salesforce_trainings",
                "description": "Training programs and participation",
            },
            {
                "name": "Travels & Expenses",
                "type": "salesforce_travels",
                "description": "Travel costs and expense tracking",
            },
            {
                "name": "Tour Plan Optimization",
                "type": "salesforce_tour_plan",
                "description": "Optimize field force tour plans",
            },
        ],
    },
    "customers": {
        "icon": "🤝",
        "color": "#2E7D32",
        "gradient": "linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%)",
        "description": "Analyze distributor, retailer, vet, doctor and farmer segments",
        "analyses": [
            {
                "name": "Distributor",
                "type": "customers_distributor",
                "description": "Distributor segment analysis",
            },
            {
                "name": "Retailer",
                "type": "customers_retailer",
                "description": "Retailer segment analysis",
            },
            {
                "name": "Vet",
                "type": "customers_vet",
                "description": "Veterinary channel analysis",
            },
            {
                "name": "Doctor",
                "type": "customers_doctor",
                "description": "Doctor/Medical channel analysis",
            },
            {
                "name": "Farmer",
                "type": "customers_farmer",
                "description": "Farmer segment analysis",
            },
        ],
    },
    "products": {
        "icon": "📦",
        "color": "#E65100",
        "gradient": "linear-gradient(135deg, #E65100 0%, #FFA726 100%)",
        "description": "Track growth patterns, inventory, and manufacturing costs",
        "analyses": [
            {
                "name": "Growth Pattern",
                "type": "products_growth",
                "description": "Product growth trends and patterns",
            },
            {
                "name": "Inventory Status",
                "type": "products_inventory",
                "description": "Current inventory levels and status",
            },
            {
                "name": "Manufacturing Cost",
                "type": "products_manufacturing",
                "description": "Manufacturing costs and efficiency",
            },
            {
                "name": "Seasonality",
                "type": "products_seasonality",
                "description": "Seasonal demand patterns",
            },
        ],
    },
    "supplychain": {
        "icon": "🚚",
        "color": "#00695C",
        "gradient": "linear-gradient(135deg, #00695C 0%, #26A69A 100%)",
        "description": "Monitor fill rates, stock levels, and warehouse operations",
        "analyses": [
            {
                "name": "Fill Rate",
                "type": "supplychain_fill_rate",
                "description": "Order fill rate and fulfillment metrics",
            },
            {
                "name": "Stock",
                "type": "supplychain_stock",
                "description": "Stock levels and availability",
            },
            {
                "name": "Back Orders",
                "type": "supplychain_backorders",
                "description": "Back order analysis and trends",
            },
            {
                "name": "Production",
                "type": "supplychain_production",
                "description": "Production scheduling and status",
            },
            {
                "name": "Warehouse",
                "type": "supplychain_warehouse",
                "description": "Warehouse operations and efficiency",
            },
        ],
    },
    "finance": {
        "icon": "💰",
        "color": "#AD1457",
        "gradient": "linear-gradient(135deg, #AD1457 0%, #F06292 100%)",
        "description": "Track outstanding, collections, credit days, and EBITDA",
        "analyses": [
            {
                "name": "Outstanding",
                "type": "finance_outstanding",
                "description": "Outstanding receivables analysis",
            },
            {
                "name": "Collections",
                "type": "finance_collections",
                "description": "Collections performance and trends",
            },
            {
                "name": "Credit Days",
                "type": "finance_credit_days",
                "description": "Days sales outstanding analysis",
            },
            {
                "name": "Bad Debt",
                "type": "finance_bad_debt",
                "description": "Bad debt and write-offs tracking",
            },
            {
                "name": "EBITDA",
                "type": "finance_ebitda",
                "description": "EBITDA and profitability metrics",
            },
        ],
    },
}
