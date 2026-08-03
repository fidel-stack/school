const inventory = [];

function findProductIndex (name){
  const productName = name.toLowerCase()
  for (let i = 0; i < inventory.length; i++){
    if (inventory[i].name === productName){
      return i;
    }
  }
  return -1;
}

console.log(findProductIndex("rice"));

function addProduct (product){
  const name = product.name.toLowerCase();
  const index = findProductIndex(name)
  if (index === -1) {
    inventory.push({name: name, quantity: product.quantity});
    console.log(`${name} added to inventory`)
  } else {
    inventory[index].quantity += product.quantity;
    console.log(`${name} quantity updated`)
  };
};
addProduct({name: "FLOUR", quantity: 5})
console.log(inventory)

function removeProduct (name, quantity){
  const productName = name.toLowerCase();
  const product = findProductIndex(productName);
  if (product === -1) {
    console.log(`${productName} not found`);
   return;
  }
  if (quantity > inventory[product].quantity) {
    console.log(`Not enough ${productName} available, remaining pieces: ${inventory[product].quantity}`)
  } else {
    inventory[product].quantity -= quantity;
    console.log(`Remaining ${productName} pieces: ${inventory[product].quantity}`);
  };
  if (inventory[product].quantity === 0) {
    inventory.splice(product, 1);
  }

};
console.log(removeProduct("FLOUR", 105))
