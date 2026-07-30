init:
	docker compose up --build -d
	docker compose exec app cp .env.example .env
	docker compose exec app composer install
	docker compose exec app php artisan key:generate
	docker compose exec app bash -c "chown -R www-data:www-data storage bootstrap/cache public && chmod -R 775 storage bootstrap/cache public"
	# Wait for MySQL to be ready
	sleep 4
	docker compose exec app php artisan migrate:fresh --seed

down:
	docker compose down -v
	docker compose down --volumes --remove-orphans

logs:
	docker compose logs -f
	# docker volume prune -f
	# docker compose down --volumes --remove-orphans
