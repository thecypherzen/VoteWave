import { NavLink } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
	faCircleUser, faBolt, faPlus, faMessage, faPowerOff
} from '@fortawesome/free-solid-svg-icons';
import styles from '../styles/pagenavitem.module.css';

export default function PageNavItem({to, type, text,
	clist=[], clickHandler=null}){
	const className = clist.join(" ");
	return (
		<li>
			<NavLink to={to}
				className={({isActive}) => {
					return isActive ?
					`${className} ${styles.navItem} ${styles.active}` :
					`${className} ${styles.navItem}`
				}}
				onClick={(e) => {clickHandler(e)}}
				>
				<span>
					<FontAwesomeIcon icon={
						type === "profile" ? faCircleUser :
						type === "action" ? faBolt :
						type === "create" ? faPlus :
						type === "inbox" ? faMessage :
						faPowerOff
					} />
				</span>
				{
					text && <span>{text}</span>
				}
			</NavLink>
		</li>
	);
}