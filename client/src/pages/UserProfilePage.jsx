import { useOutletContext } from 'react-router-dom';
import { useEffect } from 'react';
import styles from '../styles/userprofile.module.css';
import Wrapper from '../components/Wrapper';
import { setItemBg } from './UserDashboard';

export default function UserProfilePage(){
	const {user, userImgUrl } = useOutletContext();
	useEffect(() => {
		setItemBg("profile-img", userImgUrl);
	}, [user, userImgUrl]);
	return (
		<div className={styles.profile}>
			<Wrapper clist={[styles.wrapper]}>
				<div id="profile-img" className={styles.userImg}>
				</div>
				<div className={styles.info}>
					<div className={styles.infoItems}>
						<div className={styles.item}>
							<i> Prefix: </i>
							<span id="prefix">{user.prefix || "NA"}</span>
						</div>
						<div className={styles.item}>
							<i> First Name: </i>
							<span id="first_name">{user.first_name}</span>
						</div>
						<div className={styles.item}>
							<i> Last Name: </i>
							<span id="last_name">{user.last_name}</span>
						</div>
						<div className={styles.item}>
							<i> Email: </i>
							<span id="email">{user.email}</span>
						</div>
						<div className={styles.item}>
							<i> Phone: </i>
							<span id="phone">{user.phone || "NA"}</span>
						</div>
						<div className={styles.item}>
							<i> Address: </i>
							<span id="address">{user.address || "NA"}</span>
						</div>
						<div className={styles.item}>
							<i> Date of birth: </i>
							<span id="dob">{user.dob || "NA"}</span>
						</div>
					</div>
					<div className={styles.btns}>
						<button target="button" className="btn btn-primary">
							Edit
						</button>
					</div>
				</div>
			</Wrapper>
		</div>
	);
}
