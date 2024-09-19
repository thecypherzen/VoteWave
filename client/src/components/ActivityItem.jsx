import { NavLink } from 'react-router-dom';
import styles from "../styles/activityitem.module.css";
/**
 * Defines an Activity list item
 */
export default function ActivityItem({activity}){
	return (<>
	<li id={activity.id}
	 	className={styles.activityItem}
	>
		<NavLink to={`/activities/${activity.id}`}
				className={({isActive, isPending}) => {
				return isActive ? styles.activeLink :
				isPending ? styles.pendingLink : null
		}}>
			<p className={styles.pending}>
				{activity.title}
			</p>
			<div className={styles.flags}>
				<span type={activity.type}>
					{activity.type}
				</span>
				<span className={styles[activity.status]}>
					{activity.status}
				</span>
			</div>
		</NavLink>
	</li>
	</>)
}