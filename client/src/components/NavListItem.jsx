/* Defines a NavList item */
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faChevronDown } from '@fortawesome/free-solid-svg-icons'
import "../styles/navlistitem.css";

export default function NavListItem({count, text}){
	return (
		<li key={count} className="nav-list-item">
			{text} <span className="nav-item-icon"><FontAwesomeIcon icon={faChevronDown} /></span>
		</li>
	);
}