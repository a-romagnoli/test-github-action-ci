conn = new Mongo();
db = conn.getDB("unittest");

db.stock.insert({
    "store_id" : "wip_warehouse",
    "material_id" : "NM070111244",
    "quantity" : 20,
    "stock_scenario" : "20_wip"
});
db.stock.insert({
    "store_id" : "wip_warehouse",
    "material_id" : "NM070111244",
    "quantity" : 20,
    "stock_scenario" : "test_ok"
});
