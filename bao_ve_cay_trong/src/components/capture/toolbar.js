import React, { useState } from 'react';
import { StyleSheet, TouchableOpacity, View } from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome5';

const FindBugButton = ({
	style = {},
	onPressBack,
	onPressChangeCameraType,
	disabled = false,
	hide = false,
	...props
}) => {
	if (hide) return null;

	return (
		<View style={style}>
			<View style={styles.toolbar}>
				<TouchableOpacity
					style={styles.toolbarButton}
					onPress={onPressBack}>
					<Icon name='chevron-left' size={30} color='white' />
				</TouchableOpacity>
				<TouchableOpacity
					style={styles.toolbarButton}
					onPress={onPressChangeCameraType}>
					<Icon name='sync-alt' size={24} color='white' />
				</TouchableOpacity>
			</View>
		</View>
	);
};

const styles = StyleSheet.create({
	toolbarButton: {
		width: 50,
		height: 50,
		display: 'flex',
		justifyContent: 'center',
		alignItems: 'center',
	},
	toolbar: {
		flex: 1,
		display: 'flex',
		flexDirection: 'row',
		justifyContent: 'space-between',
	},
});

export default FindBugButton;
