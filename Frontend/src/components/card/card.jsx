"use client";

import React, { useState } from "react";
import "./card.css";

const Card = ({ imageSrc, location, price, status, id }) => {
  const [isFavorite, setIsFavorite] = useState(false);

  const handleToggleFavorite = () => {
    setIsFavorite(!isFavorite);
  };

  const getStatusIcon = (status) => {
    switch (status) {
      case 3:
        return "☑️";
      case 4:
        return "✅";
      case 5:
        return "❌";
    }
  };

  const getStatusName = (status) => {
    switch (status) {
      case 3:
        return "Pre venta";
      case 4:
        return "En venta";
      case 5:
        return "Vendido";
    }
  };

  const formatPrice = (price) => {
    const parts = price.toString().split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
    return parts.join('.');
  }

  return (
    <div className="card">
      <img src={imageSrc} alt="Property" className="card-image stock-image" />
      <div className="card-content flex">
        <div className="card-info">
          <h2 className="card-location">🧭 {location}</h2>
          <p className="card-price">💵 ${formatPrice(price)}</p>
          <p className="card-status">
            {getStatusIcon(status)} {getStatusName(status)}
          </p>
        </div>
        <div className="card-favorite m-auto pl-3">
          <button
            className={`card-favorite ${isFavorite ? "favorited" : ""}`}
            onClick={handleToggleFavorite}
          >
            <i className="heart-icon">{isFavorite ? "❤️" : "🤍"}</i>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Card;
