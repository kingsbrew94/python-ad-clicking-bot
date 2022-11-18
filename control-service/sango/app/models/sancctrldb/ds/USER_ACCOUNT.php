<?php namespace App\Models\sancctrldb\DS;
use FLY\Model\Algorithm\Model_Controllers;
use FLY_ENV\Util\Model\QueryBuilder;

class USER_ACCOUNT extends QueryBuilder {

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

	protected $FIRST_NAME;

	protected $LAST_NAME;

	protected $EMAIL;

	protected $PASSWORD;

	protected $STATUS;

	protected $PLAN;


	use Model_Controllers;

	public function __construct($ID="",$FIRST_NAME="",$LAST_NAME="",$EMAIL="",$PASSWORD="",$STATUS="",$PLAN="") 
	{
    	parent::__construct($this);
		$this->ID = $ID;
		$this->FIRST_NAME = $FIRST_NAME;
		$this->LAST_NAME = $LAST_NAME;
		$this->EMAIL = $EMAIL;
		$this->PASSWORD = $PASSWORD;
		$this->STATUS = $STATUS;
		$this->PLAN = $PLAN;

    	$this->pk_names=[ 'ID' ];
    	
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