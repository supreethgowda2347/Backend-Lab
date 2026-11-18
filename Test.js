const express = require('express')
const app = express();

app.use (express.json())

let products = [
    {id : 1, name : 'Laptop', price : 154000},
    {id : 2, name : 'Monitor', price : 15000},
    {id : 3, name : 'Mouse', price : 2500}
];

let next_id = 4;

app.get('/products', (req,res)=>{
    res.json(products);
});

app.post('/products', (req,res)=>{
    const product = {
        id : next_id++,
        name : req.body.name,
        price : req.body.price
    };
    products.push(product)
    res.status(201).json(product)
});

app.listen(3000, ()=>{
    console.log("Server Running on Port 3000")
});