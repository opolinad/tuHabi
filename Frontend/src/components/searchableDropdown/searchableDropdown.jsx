"use client";
import React from "react";
import Select from "react-select";
import "./searchableDropdown.css";

const SearchableDropdown = ({ options, labelName }) => {
  return (
    <div id="searchableDropdown-container">
      <label>{labelName}:</label>
      <Select
        options={options}
        isClearable={true}
        placeholder={"Seleccione..."}
      />
    </div>
  );
};

export default SearchableDropdown;
