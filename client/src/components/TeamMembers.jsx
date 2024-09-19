import Wrapper from './Wrapper';
import { Link } from 'react-router-dom';
import { classNameFromList } from '../utils/createClassNames';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
	faTwitter,
	faLinkedin,
	faGithub } from '@fortawesome/free-brands-svg-icons';
import styles from "../styles/teams.module.css";


export  function TeamMembers({children}){
	return(
	<section id={styles["teams-section"]}>
		<Wrapper clist={[styles.teamsWrapper]}>
			{children}
		</Wrapper>
	</section>
	);
}


export function TeamMember({
	first, last, role, ld, tw, gh,
	clist=null
}){
	const classname = classNameFromList(clist);
	return (
		<div className={classname}>
			<div className={styles.memberImage}>
			</div>
			<div className={styles.memberDetails}>
				<div className={styles.name}>
					<h4>{first} <span>{last}</span></h4>
					<h5>{role}</h5>
				</div>
				<div className={styles.socials}>
					<Link to={tw} className={styles.tw}
						target='blank'>
						<FontAwesomeIcon icon={faTwitter} />
					</Link>
					<Link to={ld} className={styles.ld}
						target='blank'>
						<FontAwesomeIcon icon={faLinkedin} />
					</Link>
					<Link to={gh} className={styles.gh}
						target='blank'>
						<FontAwesomeIcon icon={faGithub} />
					</Link>
				</div>
			</div>
		</div>
	);
}