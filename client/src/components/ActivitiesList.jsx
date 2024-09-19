import ActivityItem from './ActivityItem';
import '../styles/activitieslist.css';


/**
 * Activities List - a list of activity items
 */
export default function ActivitiesList(
	{ activities }){

	return (
	<aside id="activities-list"> {
		activities.length ?
			<ul>{
				activities.map((activity) => (
					<ActivityItem
						activity={activity}
						key={activity.id}
						/>
				))
			}
			</ul>
			:
			<p> No {type ? (type == 'poll' ?
				"Polls" : "Elections") : "Activities"}
					yet </p>
		}
	</aside>);
}