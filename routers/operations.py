from fastapi import APIRouter, HTTPException, status

from db_models.operation import Operation

router = APIRouter(prefix="/operations", tags=["Operations"])

@router.post("/create", response_model=Operation)
async def create_operation_based_on_strategy(operation: Operation):
    """
    Create an operation based on a strategy

    - **strategy_id**: int
    - **stop_lose_price**: float
    - **max_value**: float
    - **entry_price**: float
    - **opening_datetime**: datetime
    - **closing_datetime**: datetime
    - **asset**: str
    - **operation_type**: str
    \f
    :param operation: User input.
    """
    raise HTTPException(
            status_code=status.HTTP_501_NOT_IMPLEMENTED,
            detail="Saving an operation is not implemented yet.",
            headers={"WWW-Authenticate": "Bearer"},
        )