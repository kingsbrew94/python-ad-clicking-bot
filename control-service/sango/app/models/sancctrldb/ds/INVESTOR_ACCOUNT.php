<?php namespace App\Models\sancctrldb\DS;
use FLY\Model\Algorithm\Model_Controllers;
use FLY_ENV\Util\Model\QueryBuilder;

class INVESTOR_ACCOUNT extends QueryBuilder {

/*        
	*******************************************************************************
	* can use transaction here                                                    *
	* example: use TRANSACTION;                                                   *
	* To use a transaction specify the namespace above this model class.          *
	* That is, copy and paste the namespace: use FLY\Model\Algorithm\TRANSACTION; * 
	* right above this model class.                                               *
	*******************************************************************************
*/

	protected $ID;

	protected $USER_ID;

	protected $USERNAME;

	protected $PASSWORD;

	protected $DATE_REGISTERED;

	protected $BALANCE;

	protected $CURRENCY;

	protected $LEVEL;

	protected $VIPs;

	protected $CREDIT;


	use Model_Controllers;

	public function __construct($ID="",$USER_ID="",$USERNAME="",$PASSWORD="",$DATE_REGISTERED="",$BALANCE="",$CURRENCY="",$LEVEL="",$VIPs="",$CREDIT="") 
	{
    	parent::__construct($this);
		$this->ID = $ID;
		$this->USER_ID = $USER_ID;
		$this->USERNAME = $USERNAME;
		$this->PASSWORD = $PASSWORD;
		$this->DATE_REGISTERED = $DATE_REGISTERED;
		$this->BALANCE = $BALANCE;
		$this->CURRENCY = $CURRENCY;
		$this->LEVEL = $LEVEL;
		$this->VIPs = $VIPs;
		$this->CREDIT = $CREDIT;

    	$this->pk_names=[ 'ID' ];
    	$this->fk_names=[ 'USER_ID'=>'ID' ];
    	$this->apply();
	}


	/**
	 * @return string[]
	 * @Todo It returns the model connection credentials
	 */
	protected function connection(): array
	{
    	return array(
			'host'

				=> 'default',

			'user'

				=> 'default',

			'password'

				=> 'default',

			'model'

				=> 'default'
		);
	}
}