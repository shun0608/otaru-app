import { writable } from 'svelte/store';

export const isLoggedIn = writable(false);

export const displayLoginMessage = writable(false);

export const displayRegisterMessage = writable(false);

export async function login(email: string, password: string) {
	const response = await fetch('http://localhost:8000/login', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded'
		},
		credentials: 'include',
		body: `username=${email}&password=${password}`
	});
	if (response.status == 204) {
		isLoggedIn.set(true);
	} else {
		const data = await response.json();
		if (data) {
			isLoggedIn.set(false);
			throw new Error(data.detail);
		}
		isLoggedIn.set(false);
		throw new Error(
			'ログイン処理中にエラーが発生しました。お手数ですが、再度ログイン処理を行ってください。'
		);
	}
}
