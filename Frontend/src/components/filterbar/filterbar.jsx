'use client'
import React from 'react';
import './filterbar.css';

import SearchableDropdown from '../searchableDropdown/searchableDropdown';

const Filterbar = () => {

  const cities = [
    { value: 'barranquilla', label: 'Barranquilla' },
    { value: 'belen_de_umbria', label: 'Belén de Umbria' },
    { value: 'bogota', label: 'Bogotá' },
    { value: 'bucaramanga', label: 'Bucaramanga' },
    { value: 'cali', label: 'Cali' },
    { value: 'cartagena', label: 'Cartagena' },
    { value: 'dosquebradas', label: 'Dosquebradas' },
    { value: 'la_virginia', label: 'La Virginia' },
    { value: 'manizales', label: 'Manizales' },
    { value: 'medellin', label: 'Medellin' },
    { value: 'pereira', label: 'Pereira' }
  ]

  const years = [
    { value: '1800', label: '1800' },
    { value: '2000', label: '2000' },
    { value: '2002', label: '2002' },
    { value: '2011', label: '2011' },
    { value: '2015', label: '2015' },
    { value: '2016', label: '2016' },
    { value: '2017', label: '2017' },
    { value: '2018', label: '2018' },
    { value: '2019', label: '2019' },
    { value: '2020', label: '2020' },
    { value: '2021', label: '2021' },
    { value: '2022', label: '2022' }
  ]


  const status = [
    { value: 3, label: 'Pre venta' },
    { value: 4, label: 'En venta' },
    { value: 5, label: 'Vendido' }
  ]

  return (
    <div id="filterbar-container" className="mx-40">
      <SearchableDropdown options={cities} labelName={'Ciudad'}/>
      <SearchableDropdown options={years} labelName={'Año'}/>
      <SearchableDropdown options={status} labelName={'Estado'}/>
    </div>
  );
};

export default Filterbar;
