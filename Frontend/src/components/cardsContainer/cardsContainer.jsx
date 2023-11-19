import React from "react";
import "./cardsContainer.css";
import Card from "../card/card";
import { get } from "@/services/httpService";

const CardsContainer = async () => {
  const data = await get(`${process.env.REACT_APP_BACKEND_URL}/properties/`);

  return (
    <div className="mx-40 p-3" id="cards-container">
      {data.results.map((card) => (
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
