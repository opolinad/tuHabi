import React from 'react';
import FilterBar from '../components/filterbar/filterbar';
import CardsContainer from '../components/cardsContainer/cardsContainer';
import { get } from '../services/httpService';

const Home = async () => {
  const data = await get(`${process.env.REACT_APP_BACKEND_URL}/properties/`);

  return (
    <main>
      <FilterBar/>
      <CardsContainer cards={ data.results } />
    </main>
  )
}

export default Home;