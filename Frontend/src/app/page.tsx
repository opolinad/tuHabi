import React from 'react';
import FilterBar from '../components/filterbar/filterbar';
import CardsContainer from '../components/cardsContainer/cardsContainer';
import { get } from '../services/httpService';

const Home = async () => {
  return (
    <main>
      <FilterBar/>
      <CardsContainer />
    </main>
  )
}

export default Home;