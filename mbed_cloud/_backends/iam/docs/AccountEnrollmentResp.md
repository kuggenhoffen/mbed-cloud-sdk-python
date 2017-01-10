# AccountEnrollmentResp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the user. INVITED means that the user has not accepted the invitation request. RESET means that the password must be changed immediately. | 
**username** | **str** | A username containing alphanumerical letters and -,._@+&#x3D; characters. | 
**email_verified** | **bool** | A flag indicating whether the user&#39;s email address has been verified or not. | [optional] [default to False]
**account_id** | **str** | The UUID of the account. | 
**password_changed_time** | **int** | A timestamp of the latest change of the user password, in milliseconds. | [optional] 
**aliases** | **list[str]** | An array of aliases. | 
**groups** | **list[str]** | A list of IDs of the groups this user belongs to. | [optional] 
**created_at** | **str** | Creation UTC time RFC3339. | [optional] 
**object** | **str** | Entity name: always &#39;user&#39; | 
**is_gtc_accepted** | **bool** | A flag indicating that the General Terms and Conditions has been accepted. | [optional] [default to False]
**email** | **str** | The email address. | 
**is_marketing_accepted** | **bool** | A flag indicating that receiving marketing information has been accepted. | [optional] [default to False]
**etag** | **str** | API resource entity version. | 
**full_name** | **str** | The full name of the user. | [optional] 
**address** | **str** | Address. | [optional] 
**creation_time_millis** | **int** |  | [optional] 
**creation_time** | **int** | A timestamp of the user creation in the storage, in milliseconds. | [optional] 
**password** | **str** | The password when creating a new user. It will will generated when not present in the request. | [optional] 
**phone_number** | **str** | Phone number. | [optional] 
**id** | **str** | The UUID of the user. | 
**last_login_time** | **int** | A timestamp of the latest login of the user, in milliseconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

