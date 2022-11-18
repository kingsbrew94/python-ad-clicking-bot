<?php namespace App\Models\sancctrldb\DS;
use FLY\Model\Algorithm\Model_Controllers;
use FLY_ENV\Util\Model\QueryBuilder;

class WIDTHDRAWAL_TRANSACTION extends QueryBuilder {

/*        
	*******************************************************************************
	* can use transaction here                                                    *
	* example: use TRANSACTION;                                                   *
	* To use a transaction specify the namespace above this model class.          *
	* That is, copy and paste the namespace: use FLY\Model\Algorithm\TRANSACTION; * 
	* right above this model class.                                               *
	*******************************************************************************
*/

	protected $WID;

	protected $ACC_ID;

	protected $AMOUNT;

	protected $DATE_OF_TRAN;

	protected $STATUS;


	use Model_Controllers;

	public function __construct($WID="",$ACC_ID="",$AMOUNT="",$DATE_OF_TRAN="",$STATUS="") 
	{
    	parent::__construct($this);
		$this->WID = $WID;
		$this->ACC_ID = $ACC_ID;
		$this->AMOUNT = $AMOUNT;
		$this->DATE_OF_TRAN = $DATE_OF_TRAN;
		$this->STATUS = $STATUS;

    	$this->pk_names=[ 'WID' ];
    	$this->fk_names=[ 'ACC_ID'=>'ID' ];
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