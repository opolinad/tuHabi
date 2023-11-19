'use client'
import React, { useEffect, useState } from 'react';
import './navbar.css';

const Navbar = () => {
  const [username, setUsername] = useState(localStorage.getItem('username'));

  if (!username) {
    let userName = '';
    while (!userName.trim()) {
      userName = prompt('Cuál es su nombre de usuario');
    }
    localStorage.setItem('username', userName);
    setUsername(()=>userName);
  }

  return (
    <nav className="p-4 mx-40">
      <div className="container mx-auto flex justify-between items-center">
        {/* Logo on the left */}
        <div className="flex items-center">
          <img src="/icon.ico" alt="Logo" className="h-10 w-10" />
        </div>

        {/* Username on the right */}
        <div>
          <span className="font-semibold">{username}</span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
