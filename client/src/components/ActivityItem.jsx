import { NavLink } from 'react-router-dom';
import "../styles/activityitem.css";
/**
 * Defines an Activity list item
 */
export default function ActivityItem({activity}){
	return (<>
	<li id={activity.id}
	 	className="activity-item"
	>
		<NavLink className={(isActive, isPending) => {
			isActive ? "active" :
				isPending ? "pending" : ""
		}}>
			<p className="title">
				{activity.title}
			</p>
			<div className="flags">
				<span type={activity.type}>
					{activity.type}
				</span>
				<span className={
					activity.status == "live" ?
					"live" : "not-live"
				}>
					{activity.status}
				</span>
			</div>
		</NavLink>
	</li>
	</>)
}