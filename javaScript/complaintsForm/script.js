const fullName = document.getElementById("full-name");
const email = document.getElementById("email");
const orderNo = document.getElementById("order-no");
const productCode = document.getElementById("product-code");
const quantity = document.getElementById("quantity");
const complaintsDescription = document.getElementById("complaint-description");
const solutionDescription = document.getElementById("solution-description");
const checkBoxes = Array.from(document.querySelectorAll("#complaints-group input[type='checkbox']"));
const radioBoxes = Array.from(document.querySelectorAll("#solutions-group input[type='radio']"));
const otherCheckBox = document.getElementById("other-complaint");
const otherRadioBtn = document.getElementById("other-solution");
const complaintsGroup = document.getElementById("complaints-group");
const solutionsGroup = document.getElementById("solutions-group");
const complaintFieldset = document.getElementById("complaint-description-container");
const solutionFieldset = document.getElementById("solution-description-container");
const form = document.getElementById("form");

const fields = [
  [fullName, "full-name"],
  [email, "email"],
  [orderNo, "order-no"],
  [productCode, "product-code"],
  [quantity, "quantity"],
  [complaintsDescription, "complaint-description"],
  [solutionDescription, "solution-description"]
];

function validateForm() {
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  const regex2 = /^2024\d{6}$/;
  const regex3 = /^[a-zA-Z]{2}\d{2}-[a-zA-Z]\d{3}-[a-zA-Z]{2}\d$/;
  return {
    "full-name": fullName.value.length > 0,
    "email": regex.test(email.value),
    "order-no": regex2.test(orderNo.value),
    "product-code": regex3.test(productCode.value),
    "quantity":
      Number.isInteger(Number(quantity.value)) &&
      Number(quantity.value) > 0,
    "complaints-group": checkBoxes.some(checkbox => checkbox.checked),
    "complaint-description":
      !otherCheckBox.checked ||
      complaintsDescription.value.length >= 20,
    "solutions-group": radioBoxes.some(radio => radio.checked),
    "solution-description":
      !otherRadioBtn.checked ||
      solutionDescription.value.length >= 20
  };
}

function isValid(validationObjects) {
  return Object.values(validationObjects).every(v => v === true);
}

fields.forEach(([field, key]) => {
  field.addEventListener("change", () => {
    const validation = validateForm();

    field.style.borderColor = validation[key] ? "green" : "red";
  });
});

checkBoxes.forEach(checkBox => {
  checkBox.addEventListener("change", () => {
    const validation = validateForm();
    if (validation["complaints-group"]) {
      complaintsGroup.style.borderColor = 'green'
    }
    else {
      complaintsGroup.style.borderColor = 'red';
    }
  });
});

radioBoxes.forEach(radiobox => {
  radiobox.addEventListener("change", () => {
    const validation = validateForm();
    if (validation["solutions-group"]) {
      solutionsGroup.style.borderColor = 'green'
    }
    else {
      solutionsGroup.style.borderColor = 'red';
    }
  });
});


form.addEventListener("submit", (event) => {
  event.preventDefault();
  const validation = validateForm();
  if(!isValid(validation)) {
    Object.entries(validation).forEach(([key, value]) => {
      if(!value) {
        const field = document.getElementById(key);
        field.style.borderColor = 'red';
      }
    });
  } else {
    form.reset();
    fields.forEach(([field]) => {
      field.style.borderColor = "";
    })
    complaintsGroup.style.borderColor = "";
    solutionsGroup.style.borderColor = "";
    complaintFieldset.style.display = "none";solutionFieldset.style.display = "none";
  }
});

otherCheckBox.addEventListener("change", (event) => {
  if(event.target.checked) {
    complaintFieldset.style.display = 'block'
  } else {
    complaintFieldset.style.display = 'none'
  }
});

radioBoxes.forEach(radioBox => {
  radioBox.addEventListener("change", (event) => {
    if(event.target === otherRadioBtn && event.target.checked) {
      solutionFieldset.style.display = 'block';
    } else {
      solutionFieldset.style.display = 'none'
    }
  });
});