from fastapi import APIRouter

from .auth import router as AuthRouter
from .users import router as UsersRouter
from .products import router as ProductsRouter
from .cart import router as CartRouter
from .orders import router as OrdersRouter




router = APIRouter()

router.include_router(AuthRouter)
router.include_router(UsersRouter)
router.include_router(ProductsRouter)
router.include_router(CartRouter)
router.include_router(OrdersRouter)
