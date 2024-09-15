/* Defines the Activities Route */

import { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';

export default function Activities(){
	const location = useLocation();


	return (
		<>
			<div><h1>Activities Page</h1></div>
		</>
	);
}