const pantry = [
  { sku: "A10", name: "Tomatoes", qty: 4, expires: "2027-01-01", zone: "fridge" },
  { sku: "D43", name: "Pineapples", qty: 2, expires: "2020-01-01", zone: "general" }
];

const rawData = [
  "A10|Tomatoes|5|2027-01-01",
  "B21|Bananas|10|2027-01-01",
  "C32|Eggs|3|2027-01-01|fridge",
  "C32|Eggs|3|2027-01-01",
  "D43|Pineapples|0|2027-01-01",
  "E54|Peppers|-1|2027-01-01|fridge"
];

function parseShipment(rawData){
  const shipment = [];
  for (let i = 0; i < rawData.length; i++){
    const parts = rawData[i].split("|")
    const sku = parts[0];
    const name = parts[1];
    const qty = Number(parts[2]);
    const expires = parts[3];

    let zone = parts[4];

    if (zone === undefined){
      zone = "general";
    }

    let duplicate = false; 
    for (let j = 0; j < shipment.length; j++){
      if (shipment[j].sku === sku){
        duplicate = true;
        break;
      }
           
    }
    if (!duplicate){
      shipment.push({sku, name, qty, expires, zone
      })
      } 

  }
  return shipment;
}
function planRestock(pantry, shipment){
  const actions = [];
  for (let i = 0; i < shipment.length; i++){
    const item = shipment[i];
    if (item.qty <= 0){
      actions.push({type: "discard", item: item});
      continue;
    } else {
      let found = false;
      for (let j = 0; j < pantry.length; j++){
        if (pantry[j].sku === item.sku){
          found = true;
          break;
        }
      }
      if (found){
        actions.push({type: "restock", item: item});
        }else {
          actions.push({type: "donate", item: item})
        }
      }
  } 
  return actions;
}

function groupByZone (actions){
  const grouped = {};
  for (let i = 0; i < actions.length; i++){
    const action = actions[i];
    const zone = action.item.zone;

    if (!grouped[zone]){
      grouped[zone] = [];
    }
    grouped[zone].push(action)
  }
  return grouped;
}

function clonePantry(pantry){
  const copy = [];

  for(let i = 0; i < pantry.length; i++){
    const item = pantry[i];
    copy.push({sku: item.sku, name: item.name, qty: item.qty, expires: item.expires, zone: item.zone});
  }
  return copy;
}

const shipment = parseShipment(rawData);
const actions = planRestock(pantry, shipment);
const grouped = groupByZone(actions)

console.log(shipment);
console.log(actions);
console.log(grouped);