import redis from 'redis';
import { promisify } from 'util';
const express = require('express');
const app = express()
const port = 1245;

const client = redis.createClient()

const listProducts = [
	{id: 1, name: "Suitcase 250", price: 50, stock: 4},
	{id: 2, name: "Suitcase 450", price: 100, stock: 10},
	{id: 3, name: "Suitcase 650", price: 350, stock: 2},
	{id: 4, name: "Suitcase 1050", price: 550, stock: 5}
];

const getItemById = function(id) {
	return listProducts.find(product => product.id === id);
};

app.get('/list_products', (req, res) => {
	res.json(listProducts);
});

const reserveStockById = function(itemId, stock) {
	client.set(`item.${itemId}`, stock);

}

async function getCurrentReservedStockById(itemId) {
	const getAsync = promisify(client.get).bind(client);
	try {
		const value = await getAsync(`item.${itemId}`);
		return value ? parseInt(value) : 0;
	} catch (error) {
		console.log('Error fetching value:', error);
    }
}

app.get('/list_products/:itemId(\\d+)', async (req, res) => {
	const itemId = parseInt(req.params.itemId);
	const product = getItemById(itemId);

	if (!product) {
		return res.status(404).json({ status: 'Product not found' });
	}
	
	res.json(product);
});

app.get('/reserve_product/:itemId(\\d+)', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);
    const stock = await getCurrentReservedStockById(itemId);

    if (!product) {
        return res.status(404).json({ status: 'Product not found' });
    }

    if (product.stock <= 0) {
        return res.status(400).json({ status: 'Not enough stock available', itemId: itemId });
    }

    if (product.stock > 0) {
        reserveStockById(itemId, 1);
        return res.status(200).json({ status: 'Reservation confirmed', itemId: itemId });
    }
});

client.on('connect', function() {
    console.log('Connected to Redis server');
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
