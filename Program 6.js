const express = require('express');
const app = express();

app.use((req, res,next) => {
    console.log(`[${new Date().toISOString()}]
        ${req.method} ${req.url}`);
    next();
});
let products = [
    {id : 1, name : 'Laptop' , price : 75000}
];

let nextId = 2;

// GET all products

app.get('/products',(req,res) => {
    res.json(products);
});

// POST a new product

app.post('/products', (req,res) => {
    const {name,price} = Request.body;

    if (!name || name.trim() === ''){
        return res.status(400).json({
            error: 'Product name is required and cannot be empty'
        });
    }

    if (! price || price <=0) {
        return res.status(400).json({
            error: 'Product price must be greater than 0'
        });
    }

    const product = {
        id : nextId++,
        name,
        price
    };

    products.push(product);

    res.status(201).json(product);
});

app.listen(3000, () => {
 console.log('Server on port 3000')});

