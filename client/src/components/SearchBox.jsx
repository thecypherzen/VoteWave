/* Defines a Searchbox */
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {useState} from 'react';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import SearchSpinner from './SearchSpinner'
import '../styles/searchbox.css';



export default function SearchBox({ph, id, valueSetter}){
	const [term, setTerm] = useState("");
	return (
		<>
			<form onSubmit={(e) => {
				e.preventDefault();
				valueSetter(term);
			}}id={id} className="search-box"
				role="search">
				<div className="search-icon-box">
					<FontAwesomeIcon icon={faSearch} />
				</div>
				<input
					onChange={(e) => {
						setTerm(e.target.value);
					}}
					type="text"
					name="search"
					role="search"
					placeholder={ph}
				/>
				<div id="search-spinner"
				className="hidden">
					<SearchSpinner/>
				</div>
			</form>
		</>
	);
}
