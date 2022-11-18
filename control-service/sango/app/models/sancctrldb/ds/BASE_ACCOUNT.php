<?php namespace App\Models\sancctrldb\DS;
use FLY\Model\Algorithm\Model_Controllers;
use FLY_ENV\Util\Model\QueryBuilder;

class BASE_ACCOUNT extends QueryBuilder {

/*        
	*******************************************************************************
	* can use transaction here                                                    *
	* example: use TRANSACTION;                                                   *
	* To use a transaction specify the namespace above this model class.          *
	* That is, copy and paste the namespace: use FLY\Model\Algorithm\TRANSACTION; * 
	* right above this model class.                                               *
	*******************************************************************************
*/

	protected $BID;

	protected $PACCT;

	protected $CACCT;


	use Model_Controllers;

	public function __construct($BID="",$PACCT="",$CACCT="") 
	{
    	parent::__construct($this);
		$this->BID = $BID;
		$this->PACCT = $PACCT;
		$this->CACCT = $CACCT;

    	$this->pk_names=[ 'BID' ];
    	$this->fk_names=[ 'PACCT'=>'ID' ];
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