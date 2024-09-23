import { useEffect, useState } from 'react';
import styles from '../styles/alert.module.css';
export default function Alert({message, error=false, success=false}){
	useEffect(() => {
		if (message){
			showMessage(message, error ? styles.error :
								success ? styles.success :
								styles.neutral);
		}
	}, [message]);
	return (
		<div id="alert" className={styles.alertBox}>
		</div>
	);
}

function showMessage(content, classname){
	const msgParent = document.getElementById("alert");
	if (msgParent){
		const message = document.createElement("p");
		message.textContent = `${content}`;
		message.classList.add(styles.alertMsg, classname);
		msgParent.appendChild(message);
		setTimeout(() => {
			message.remove();
		}, 50000)
	}
}