import React from "react";
import "./cardsContainer.css";
import Card from "../card/card";

const CardsContainer = ({ cards }) => {
  return (
    <div className="mx-40 p-3" id="cards-container">
      {cards.map((card) => (
        <Card
          id={card.id}
          location={card.city}
          price={card.price}
          status={card.actual_status}
        />
      ))}
    </div>
  );
};

export default CardsContainer;
