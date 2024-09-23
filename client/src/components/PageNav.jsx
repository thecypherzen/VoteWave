import { useEffect, useState } from 'react';
import { useLoaderData } from  'react-router-dom';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
	faCircleChevronLeft, faCircleChevronRight, faBell
} from '@fortawesome/free-solid-svg-icons';
import PageNavItem from './PageNavItem';
import { getLogoutUrl } from '../pages/LoginPage';
import styles from '../styles/pagenav.module.css';

export default function PageNav({owner}){
	//const userId = useLoaderData();
	//const [anyError, setAnyError] = useState(false);
	//const [errMsg, setErrMsg] = useState(null);

	return (
		<section className={styles.pageNav}>
			<div className={styles.owner}>
				<div id="nav-owner-icon" className={styles.ownerIcon}>

				</div>
				<div className={styles.ownerInfo}>
					<h3>{owner.first_name}William</h3>
				</div>
			</div>
			<div className={styles.btns}>
				<div className={styles.arrows}>
					<span id="nav-back" className={styles.backBtn}>
						<FontAwesomeIcon icon={faCircleChevronLeft} />
					</span>
					<span id="nav-fwd" className={styles.fwdBtn}>
						<FontAwesomeIcon icon={faCircleChevronRight} />
					</span>
				</div>
				<span className={styles.bell}>
					<FontAwesomeIcon icon={faBell} />
				</span>
			</div>
			<ul className={styles.navList}>
				<PageNavItem
					to=""
					type="profile"
					text="Profile"
					clist={[styles.listItem]}
				/>
				<PageNavItem
					to=""
					type="action"
					text="My Activities"
					clist={[styles.listItem]}
				/>
				<PageNavItem
					to=""
					text="Create"
					type="create"
					clist={[styles.listItem]}
				/>
				<PageNavItem
					to=""
					text="Inbox"
					type="inbox"
					clist={[styles.listItem]}
				/>
				<PageNavItem
					clist={[styles.listItem, styles.logout]}
					text="Logout"
					clickHandler={handleLogout}
				/>

			</ul>
			<div className={styles.product}>
				<div className={styles.logo}>
				</div>
				<p>VoteWave &copy; 2024</p>
			</div>
		</section>
	);
}

export function loader({params}){
	return params?.userId ?? null;
}


/* handle logout click */
const handleLogout = function (event){
	event.preventDefault();
	window.location.href = getLogoutUrl();
}
