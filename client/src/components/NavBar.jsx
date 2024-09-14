/* Defines the NavBar component */

import NavListItem from './NavListItem';
import SearchBox from './SearchBox';
import '../styles/navbar.css'


export default function NavBar(){
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
				<div>
					<SearchBox
						id="nav-search-form"
						ph="Find ongoing activities"
					/>
				</div>
				<div id="nav-btn">
					<a id="signin-btn"
					className="btn btn-secondary"
					href="#">Login/Sign up</a>
				</div>
			</div>
		</nav>
	);
}