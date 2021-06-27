import { PermissionsAndroid, Platform } from 'react-native';

export const checkPermission = async permission => {
	return await PermissionsAndroid.check(permission);
};

export const requestPermission = async permission => {
	return await PermissionsAndroid.request(permission);
};

export const hasAndroidPermission = async permission => {
	const hasPermission = await PermissionsAndroid.check(permission);
	if (hasPermission) {
		return true;
	}

	const status = await PermissionsAndroid.request(permission);
	return status === 'granted';
};

export const hasReadExternalStoragePermission = async () => {
	const permission = PermissionsAndroid.PERMISSIONS.READ_EXTERNAL_STORAGE;
	return await hasAndroidPermission(permission);
};
