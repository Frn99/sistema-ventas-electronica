// Contenido completo para frontend/src/components/ProductList.jsx

import React, { useState, useEffect } from 'react';

function ProductList() {
  // 'products' guardará la lista de productos que recibamos de la API
  const [products, setProducts] = useState([]);
  // 'error' guardará cualquier error que ocurra durante la petición
  const [error, setError] = useState(null);
  // 'loading' nos indicará si la petición está en curso
  const [loading, setLoading] = useState(true);

  // useEffect se ejecuta cuando el componente se monta por primera vez
  useEffect(() => {
    // Hacemos la petición a nuestra API de Django
    fetch('http://127.0.0.1:8000/api/productos/')
      .then(response => {
        if (!response.ok) {
          throw new Error('La respuesta de la red no fue satisfactoria');
        }
        return response.json();
      })
      .then(data => {
        setProducts(data); // Actualizamos el estado con los datos recibidos
        setLoading(false); // La carga ha terminado
      })
      .catch(error => {
        setError(error); // Guardamos el error para mostrarlo
        setLoading(false); // La carga ha terminado (incluso con error)
      });
  }, []); // El array vacío asegura que el efecto se ejecute solo una vez

  if (loading) {
    return <div>Cargando productos...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Nuestros Productos</h1>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <h2>{product.nombre}</h2>
            <p>Precio: ${product.precio}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;