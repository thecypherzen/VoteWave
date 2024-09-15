/* Defines the NavBar component */

import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Button from './Button';
import NavListItem from './NavListItem';
import SearchBox from './SearchBox';
import '../styles/navbar.css'

export default function NavBar(){
	const [searchValue, setSearchValue] = useState("");
	const navigate = useNavigate();

	useEffect(() => {
		if (searchValue) {
			navigate("/activities",
				{state: {searchTerm: searchValue}});
		}
	}, [searchValue]);

	return (
		<nav id="navbar">
			<div className="nav-wrapper">
				<div id="nav-logo">
					<div id="logo-icon"></div>
					<h2 id="logo-text">VoteWave</h2>
				</div>
				<div id="nav-list-wrapper">
					<ul className="nav-list">
						<NavListItem count={1} text="Quick Guide"/>
						<NavListItem count={2} text="Games"/>
					</ul>
				</div>
				<div id="nav-btns">
					<div>
						<Button
							clist={["btn", "btn-accent"]}
							id="search-btn" href="/activities"
							text="Live Activities"
						/>
					</div>
					<div id="login-btn">
						<Button
							clist={["btn", "btn-secondary"]}
							id="signin-btn" href="#"
							text="Login/Sign up"
						/>
					</div>
				</div>
			</div>
		</nav>
	);
}