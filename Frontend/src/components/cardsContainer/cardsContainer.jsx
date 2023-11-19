import React from "react";
import "./cardsContainer.css";
import Card from "../card/card";

const CardsContainer = ({ cards }) => {
  const imgSrc =
    "https://thumbor.forbes.com/thumbor/fit-in/900x510/https://www.forbes.com/home-improvement/wp-content/uploads/2022/07/download-23.jpg";

  return (
    <div className="mx-40 p-3" id="cards-container">
      {cards.map((card) => (
        <Card
          id={card.id}
          imageSrc={imgSrc}
          location={card.city}
          price={card.price}
          status={card.actual_status}
        />
      ))}
    </div>
  );
};

export default CardsContainer;
