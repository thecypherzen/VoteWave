/* Defines a Searchbox */
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';
import SearchSpinner from './SearchSpinner'
import '../styles/searchbox.css';


export default function SearchBox({ph, id}){
	return (
		<>
			<form id={id} className="search-box"
				role="search">
				<div className="search-icon-box">
					<FontAwesomeIcon icon={faSearch} />
				</div>
				<input
					type="text"
					name="search"
					role="search"
					placeholder={ph}
				/>
				<div id="search-spinner"
				class="hidden">
					<SearchSpinner/>
				</div>
			</form>
		</>
	);
}