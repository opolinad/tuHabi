import React from "react";
import "./cardsContainer.css";
import Card from "../card/card";
import { get } from "@/services/httpService";

const CardsContainer = async () => {
  let url = `${process.env.REACT_APP_BACKEND_URL}/properties/`;
  const data = await get(url);

  return (
    <div className="mx-40 p-3" id="cards-container">
      {data.results.length ? (
        data.results.map((card) => (
          <Card
            id={card.id}
            location={card.city}
            price={card.price}
            status={card.actual_status}
          />
        ))
      ) : (
        <p id="no-results-to-show">No hay resultados para mostrar</p>
      )}
    </div>
  );
};

export default CardsContainer;
